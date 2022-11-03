__author__ = "Caspar Schmitt"
__copyright__ = (
    "Copyright 2022, Caspar Schmitt & b2luigi (https://github.com/nils-braun/b2luigi)"
)
__email__ = "cschmitt@mpp.mpg.de"
__license__ = "free"

# source: adapted from b2luigi (https://github.com/nils-braun/b2luigi)
import errno
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import warnings
from collections import Counter
from datetime import datetime
from functools import lru_cache
from glob import glob
from itertools import groupby
from typing import Iterable, List, Optional, Set
from getpass import getpass

from jinja2 import Template
from retry import retry
import time

gbasf2_min_proxy_lifetime = snakemake.params.get("gbasf2_min_proxy_lifetime", 0)
gbasf2_proxy_lifetime = snakemake.params.get("gbasf2_proxy_lifetime", 24)
gbasf2_dataset = snakemake.params.get("gbasf2_dataset", "")
release = snakemake.params.get("release", "")
maxretries = snakemake.params.get("gbasf2_max_retries", 3)
download_logs = snakemake.params.get("gbasf2_download_logs", True)
steeringfile = snakemake.params.get("steeringfile", "")
sandbox_input_files = snakemake.params.get("sandbox_input_files", [])
outname = snakemake.params.get("gbasf2_output_file_name", "")
output_filelist = snakemake.output.get("output_filelist", "")
proxy_text_file = snakemake.output.get("proxy_text_file", "proxy.dat")
setProxy = snakemake.params.get("setProxy", False)


class Gbasf2Process:
    def __init__(
        self,
        gbasf2_dataset,
        steering_file,
        release,
        sandbox_files,
        maxtries,
        outname,
        skimfiles,
        download_log_files=True,
        SetupOnly=False,
    ):
        self.dirac_user = get_dirac_user()
        self.gbasf2_project_name = hashlib.md5(gbasf2_dataset.encode()).hexdigest()
        self._command = [
            "gbasf2",
            steering_file,
            "-p",
            self.gbasf2_project_name,
            "-i",
            gbasf2_dataset,
            "-s",
            release,
        ]
        if len(sandbox_files) > 0:
            self._command.append("-f")
            self._command += sandbox_files
        self._command.append("--force")
        self._n_jobs_by_status = ""
        self.max_retries = maxtries
        self.wantLogs = download_log_files
        self._project_had_been_successful = False
        self._outname = outname
        self._steeringfile = steering_file
        self._skimfiles = skimfiles
        # Store number of times each job had been rescheduled
        self.n_retries_by_job = Counter()

    def start_job(self):
        self._log = f"{os.path.splitext(self._skimfiles)[0]}_log.dat"
        if check_project_exists(self.gbasf2_project_name, self.dirac_user):
            print(
                f"\nProject with name {self.gbasf2_project_name} already exists on grid, "
                "therefore not submitting new project. If you want to submit a new project, "
                "change the project name."
            )
            return
        log = open(self._log, "a")
        log.write(f"submitting LCGrid job with command {self._command}\n")
        proc = run_with_gbasf2(
            self._command,
            cwd=os.path.dirname(self._steeringfile),
            ensure_proxy_initialized=True,
            capture_output=True,
            check=True,
        )  # execute this in steering file directory!
        # Check if there were any errors, since gb2_proxy_init often still exits without errorcode and sends messages to stdout
        out, err = proc.stdout, proc.stderr
        all_output = (
            out + err
        )  # gb2_proxy_init errors are usually in stdout, but for future-proofing also check stderr
        print(all_output)
        log.write(all_output + "\n")
        log.close()

    def get_job_id(self):
        return self.gbasf2_project_name

    def get_job_status(self):
        """
        Get overall status of the gbasf2 project.

        First obtain the status of all (sub-) jobs in a gbasf2 project, similar
        to ``gb2_job_status``, and return an overall project status, e.g. when
        all jobs are done, return ``JobStatus.successful`` to show that the
        gbasf2 project succeeded.
        """
        job_status_dict = get_gbasf2_project_job_status_dict(
            self.gbasf2_project_name, dirac_user=self.dirac_user
        )
        n_jobs_by_status = Counter()
        for _, job_info in job_status_dict.items():
            n_jobs_by_status[job_info["Status"]] += 1

        # recheck the status more closely, and correct
        # reason: sometimes 'Status' marked as 'Done',
        # while 'ApplicationStatus' is not 'Done'
        for _, job_info in job_status_dict.items():
            if job_info["Status"] == "Done" and (
                job_info["ApplicationStatus"] != "Done"
            ):
                n_jobs_by_status["Done"] -= 1
                n_jobs_by_status["Failed"] += 1

        job_status_string = str(dict(sorted(n_jobs_by_status.items()))).strip("{}")
        print(f"{job_status_string}")
        self._n_jobs_by_status = n_jobs_by_status

        n_jobs = len(job_status_dict)
        n_done = n_jobs_by_status["Done"]
        # note: "Killed" jobs also get moved to "Failed" after a while
        n_failed = n_jobs_by_status["Failed"]
        n_in_final_state = n_done + n_failed

        # The gbasf2 project is considered as failed if any of the jobs in it failed.
        # However, we first try to reschedule thos jobs and only declare it as failed if the maximum number of retries
        # for reschedulinhas been reached
        if n_failed > 0:
            if self.max_retries > 0 and self._reschedule_failed_jobs():
                return "RUN"
            self._on_failure_action()
            return "ABORTED FAILED JOB"

        # task is running
        if n_in_final_state < n_jobs:
            return "RUN"

        # Require all jobs to be done for project success, any job failure results in a failed project
        if n_done == n_jobs:
            # download dataset only the first time that we return JobStatus.successful
            if not self._project_had_been_successful:
                try:
                    self._on_first_success_action()
                    self._project_had_been_successful = True
                # RuntimeError might occur when download of output dataset was not complete. This is
                # frequent, so we want to catch that error and just marking the job as failed
                except RuntimeError as err:
                    warnings.warn(repr(err), RuntimeWarning)
                    return "ABORTED FAILED DOWNLOAD"

            return "DONE"

        raise RuntimeError("Could not determine JobStatus")

    def _on_first_success_action(self):
        pass
        """
        Things to do after all jobs in the project had been successful, e.g. downloading the dataset and logs
        """
        if self.wantLogs:
            self._download_logs()
        self._download_dataset()

    def _on_failure_action(self):
        """
        Things to do after the project failed
        """
        job_status_dict = get_gbasf2_project_job_status_dict(
            self.gbasf2_project_name, dirac_user=self.dirac_user
        )
        failed_job_dict = {
            job_id: job_info
            for job_id, job_info in job_status_dict.items()
            if job_info["Status"] == "Failed"
            or (
                job_info["Status"] == "Done" and job_info["ApplicationStatus"] != "Done"
            )
        }
        n_failed = len(failed_job_dict)
        log = open(self._log, "a")
        log.write(f"{n_failed} failed jobs:\n{failed_job_dict}\n")
        log.close()
        self._download_logs()

    def _reschedule_failed_jobs(self):
        """
        Tries to reschedule failed jobs in the project if ``self.max_retries`` has not been reached
        and returns ``True`` if rescheduling has been successful.
        """
        jobs_to_be_rescheduled = []
        jobs_hitting_max_n_retries = []
        job_status_dict = get_gbasf2_project_job_status_dict(
            self.gbasf2_project_name, dirac_user=self.dirac_user
        )

        for job_id, job_info in job_status_dict.items():
            if job_info["Status"] == "Failed" or (
                job_info["Status"] == "Done" and job_info["ApplicationStatus"] != "Done"
            ):
                if self.n_retries_by_job[job_id] < self.max_retries:
                    self.n_retries_by_job[job_id] += 1
                    jobs_to_be_rescheduled.append(job_id)
                else:
                    jobs_hitting_max_n_retries.append(job_id)

        if jobs_to_be_rescheduled:
            self._reschedule_jobs(jobs_to_be_rescheduled)

        if jobs_hitting_max_n_retries:
            warnings.warn(
                f"Reached maximum number of rescheduling tries ({self.max_retries}) for following jobs:\n\t"
                + "\n\t".join(str(j) for j in jobs_hitting_max_n_retries)
                + "\n",
                RuntimeWarning,
            )
            return False

        return True

    def _reschedule_jobs(self, job_ids):
        """
        Reschedule chosen list of jobs.
        """
        log = open(self._log, "a")
        log.write("Rescheduling jobs:\n")
        log.write(
            "\t"
            + "\n\t".join(
                f"{job_id} ({self.n_retries_by_job[job_id]} retries)\n"
                for job_id in job_ids
            )
        )
        log.close()
        print("Rescheduling jobs...")
        reschedule_command = shlex.split(
            f"gb2_job_reschedule --jobid {' '.join(job_ids)} --force"
        )
        run_with_gbasf2(reschedule_command)

    def _get_gbasf2_dataset_query(self, output_file_name):
        """
        Helper method that returns the gbasf2 query string with the correct wildcard pattern
        to get the subset of all files for ``output_file_name`` from the grid project associated with this task,
        either, e.g. via the ``gb2_ds_list`` or ``gb2_ds_get`` commands.

        Args:
            output_file_name: Output file name, must be a root file, e.g. ``ntuple.root``.
        """
        if output_file_name != os.path.basename(output_file_name):
            raise ValueError(
                f'For grid projects, the output file name must not be a basename, not a path, but is "{output_file_name}"'
            )
        output_file_stem, output_file_ext = os.path.splitext(output_file_name)
        if output_file_ext != ".root":
            raise ValueError(
                f'Output file name "{output_file_name}" does not end with ".root", '
                "but gbasf2 batch only supports root outputs"
            )
        dataset_query_string = f"/belle/user/{self.dirac_user}/{self.gbasf2_project_name}/sub*/{output_file_stem}_*{output_file_ext}"
        return dataset_query_string

    def _local_gb2_dataset_is_complete(self, output_dir_path, output_file_name):
        """
        Helper method that returns ``True`` if the download of the gbasf2
        dataset for the output ``output_file_name`` is complete.

        Args:
            output_file_name: Output file name, must be a root file, e.g. ``ntuple.root``.
                Usually defined by the user via :py:func:`b2luigi.Task.add_to_output` in
        """
        # first get the local set of files in the dataset for `output_file_name`
        glob_expression = os.path.join(
            f"{output_dir_path}", self.gbasf2_project_name, "sub*", "*.root"
        )
        downloaded_dataset_basenames = [
            os.path.basename(fpath) for fpath in glob(glob_expression)
        ]
        #         downloaded_dataset_basenames = [file for file in os.listdir(output_dir_path) if(file.endswith(".root"))]

        if not downloaded_dataset_basenames:
            return False

        # get the remote set of grid file names for the gbasf2 project output matching output_file_name
        ds_query_string = self._get_gbasf2_dataset_query(output_file_name)
        output_dataset_grid_filepaths = query_lpns(ds_query_string)
        output_dataset_basenames = [
            os.path.basename(grid_path) for grid_path in output_dataset_grid_filepaths
        ]
        # remove duplicate LFNs that gb2_ds_list returns for outputs from rescheduled jobs
        output_dataset_basenames = get_unique_lfns(output_dataset_basenames)
        # check if local and remote datasets are equal
        if set(output_dataset_basenames) == set(downloaded_dataset_basenames):
            return True
        return False

    def _download_dataset(self):
        """
        Download the task outputs from the gbasf2 project dataset.

        For each task output defined via ``self.add_to_output(<name>.root)`` a
        directory will be created, into which all files named ``name_*.root`` on
        the grid dataset corresponding to the project name will be downloaded.
        The download is ensured to be automatic by first downloading into
        temporary directories.
        """
        output_dir_path = os.path.dirname(self._log)
        if output_dir_path == "":
            output_dir_path = "."
        dataset_query_string = self._get_gbasf2_dataset_query(self._outname)

        # check if dataset had been already downloaded and if so, skip downloading
        log = open(self._log, "a")
        if os.path.isdir(output_dir_path) and self._local_gb2_dataset_is_complete(
            output_dir_path, self._outname
        ):
            log.write(
                f"Dataset already exists in {output_dir_path}, skipping download.\n"
            )

        else:
            log.write(f"Downloading dataset in {output_dir_path}.\n")

            if not check_dataset_exists_on_grid(
                self.gbasf2_project_name, dirac_user=self.dirac_user
            ):
                raise RuntimeError(
                    f"Not dataset to download under project name {self.gbasf2_project_name}"
                )

            print("Downloading datasets...")
            ds_get_command = shlex.split(f"gb2_ds_get --force {dataset_query_string}")
            log.write(
                f"Downloading dataset into\n  {output_dir_path}\n  with command\n  "
                + " ".join(ds_get_command)
                + "\n"
            )

            download_retries = 0  # try this download 3 times
            while (
                not self._local_gb2_dataset_is_complete(output_dir_path, self._outname)
                and download_retries < 3
            ):
                stdout = run_with_gbasf2(
                    ds_get_command, cwd=output_dir_path, capture_output=True
                ).stdout
                log.write(stdout + "\n")
                if "No file found" in stdout:
                    raise RuntimeError(
                        f"No output data for gbasf2 project {self.gbasf2_project_name} found."
                    )
                download_retries += 1

            if not self._local_gb2_dataset_is_complete(output_dir_path, self._outname):
                raise RuntimeError(
                    f"Download incomplete. The downloaded set of files in {output_dir_path} is not equal to the "
                    + f"list of dataset files on the grid for project {self.gbasf2_project_name}.",
                )

        log.write(f"Download of {self.gbasf2_project_name} files successful.\n")
        with open(self._skimfiles, "w") as skim_files:
            files = []
            listing = os.listdir(f"{output_dir_path}/{self.gbasf2_project_name}/")
            for subdir in listing:  # go through the /sub*
                path = f"{output_dir_path}/{self.gbasf2_project_name}/{subdir}/"
                files += [
                    path + file for file in os.listdir(path) if (file.endswith(".root"))
                ]
            skim_files.write(json.dumps(files))
        log.write(f"file directories written to {self._skimfiles}\n")
        log.close()
        print("Download successful.")

    def _download_logs(self):
        """
        Download sandbox files from grid with logs for each job in the gbasf2 project.

        It wraps ``gb2_job_output``, which downloads the job sandbox, which has the following structure:

        .. code-block:: text

            log
            └── <project name>
                ├── <first job id>
                │   ├── job.info
                │   ├── Script1_basf2helper.py.log # basf2 outputs
                │   └── std.out
                ├── <second job id>
                │   ├── ...
                ...

        These are stored in the task log dir.
        """
        logpath = os.path.dirname(self._log)
        if logpath == "":
            logpath = "."
        download_logs_command = shlex.split(
            f"gb2_job_output --user {self.dirac_user} -p {self.gbasf2_project_name}"
        )
        print("Downloading logs...")
        stdout = run_with_gbasf2(
            download_logs_command, cwd=logpath, capture_output=True
        ).stdout
        log = open(self._log, "a")
        log.write(stdout + "\n")
        log.write(
            f"Download of logs for gbasf2 project {self.gbasf2_project_name} successful.\n"
        )
        log.close()

    def kill_job(self):
        """
        Kill gbasf2 project
        """
        if not check_project_exists(
            self.gbasf2_project_name, dirac_user=self.dirac_user
        ):
            return
        # Note: The two commands ``gb2_job_delete`` and ``gb2_job_kill`` differ
        # in that deleted jobs are killed and removed from the job database,
        # while only killed jobs can be restarted.
        command = shlex.split(
            f"gb2_job_kill --force --user {self.dirac_user} -p {self.gbasf2_project_name}"
        )
        run_with_gbasf2(command)


def check_dataset_exists_on_grid(gbasf2_project_name, dirac_user=None):
    """
    Check if an output dataset exists for the gbasf2 project
    """
    lpns = query_lpns(gbasf2_project_name, dirac_user=dirac_user)
    return len(lpns) > 0


def get_gbasf2_project_job_status_dict(gbasf2_project_name, dirac_user=None):
    """
    Returns a dictionary for all jobs in the project with a structure like the
    following, which I have taken and adapted from an example output::
        {
            "<JobID>": {
                "SubmissionTime": "2020-03-27 13:08:49",
                "Owner": "<dirac username>",
                "JobGroup": "<ProjectName>",
                "ApplicationStatus": "Done",
                "HeartBeatTime": "2020-03-27 16:01:39",
                "Site": "LCG.KEK.jp",
                "MinorStatus": "Execution Complete",
                "LastUpdateTime": "2020-03-27 16:01:40",
                "Status": "<Job Status>"
            }
        ...
        }
    For that purpose, the script in ``gbasf2_job_status.py`` is called.  That
    script directly interfaces with Dirac via its API, but it only works with
    the gbasf2 environment and python2, which is why it is called as a
    subprocess.  The job status dictionary is passed to this function via json.
    """
    if dirac_user is None:
        dirac_user = get_dirac_user()
    job_status_script_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "gbasf2_job_status.py"
    )
    job_status_command = shlex.split(
        f"{job_status_script_path} -p {gbasf2_project_name} --user {dirac_user}"
    )
    proc = run_with_gbasf2(job_status_command, capture_output=True, check=False)
    # FIXME: use enum or similar to define my own return codes
    if proc.returncode == 3:  # return code 3 means project does not exist yet
        raise RuntimeError(
            f"\nCould not find any jobs for project {gbasf2_project_name} on the grid.\n"
            + "Probably there was an error during the project submission when running the gbasf2 command.\n"
        )
    job_status_json_string = proc.stdout
    return json.loads(job_status_json_string)


def check_project_exists(gbasf2_project_name, dirac_user=None):
    """
    Check if we can find the gbasf2 project on the grid with ``gb2_job_status``.
    """
    try:
        return bool(get_gbasf2_project_job_status_dict(gbasf2_project_name, dirac_user))
    except RuntimeError:
        return False


def run_with_gbasf2(
    cmd,
    *args,
    ensure_proxy_initialized=True,
    check=True,
    encoding="utf-8",
    capture_output=False,
    **kwargs,
):
    """
    Call ``cmd`` in a subprocess with the gbasf2 environment.
    :param ensure_proxy_initialized: If this is True, check if the dirac proxy is initalized and alive and if not,
                                     initialize it.
    :param check: Whether to raise a ``CalledProcessError`` when the command returns with an error code.
                  The default value ``True`` is the same as in ``subprocess.check_call()`` and different as in the
                  normal ``run_with_gbasf2()`` command.
    :param capture_output: Whether to capture the ``stdout`` and ``stdin``.
                           Same as setting them to in ``subprocess.PIPE``.
                           The implementation of this argument was taken from the ``subprocess.run()`` in python3.8.
    :param encoding: Encoding to use for the interpretation of the command output.
                     Different from normal subprocess commands, it by default assumes "utf-8". In that case, the returned
                     ``stdout`` and ``stderr`` are strings and not byte-strings and the user doesn't have to decode them
                     manually.
    :return: ``CompletedProcess`` instance
    """
    if capture_output:
        if kwargs.get("stdout") is not None or kwargs.get("stderr") is not None:
            raise ValueError(
                "stdout and stderr arguments may not be used " "with capture_output."
            )
        kwargs["stdout"] = subprocess.PIPE
        kwargs["stderr"] = subprocess.PIPE
    gbasf2_env = get_gbasf2_env()
    if ensure_proxy_initialized:
        setup_dirac_proxy()
    proc = subprocess.run(
        cmd, *args, check=check, encoding=encoding, env=gbasf2_env, **kwargs
    )
    return proc


def get_gbasf2_env(gbasf2_install_directory=None):
    """
    Return the gbasf2 environment dict which can be used to run gbasf2 commands.
    :param gbasf2_install_directory: Directory into which gbasf2 has been
        installed.  When set to the default value ``None``, it looks for the
        value of the ``gbasf2_install_directory`` setting and when that is not
        set, it uses the default of most installation instructions, which is
        ``~/gbasf2KEK``.
    :return: Dictionary containing the  environment that you get from sourcing the gbasf2 setup script.
    """
    if gbasf2_install_directory is None:
        # Use the latest gbasf2 release on CVMFS as the default gbasf2 install directory.
        # To get the directory of the latest release, take the parent of the "pro"
        # symlink which points to a sub-directory of the latest release.
        default_gbasf2_install_directory = os.path.realpath(
            os.path.join("/cvmfs/belle.kek.jp/grid/gbasf2/pro", os.pardir, os.pardir)
        )
        gbasf2_install_directory = default_gbasf2_install_directory
    gbasf2_setup_path = os.path.join(
        gbasf2_install_directory, "BelleDIRAC/gbasf2/tools/setup.sh"
    )
    if not os.path.isfile(gbasf2_setup_path):
        raise FileNotFoundError(
            f"Could not find gbasf2 setup file at:\n{gbasf2_setup_path}.\n"
            f"Make sure that `gbasf2_install_directory` is set correctly. Current setting:\n{gbasf2_install_directory}.\n"
        )
    # complete bash command to set up the gbasf2 environment
    # piping output to /dev/null, because we want that our final script only prints the ``env`` output
    gbasf2_setup_command_str = f"source {gbasf2_setup_path} > /dev/null"
    # command to execute the gbasf2 setup command in a fresh shell and output the produced environment
    echo_gbasf2_env_command = shlex.split(
        f"env -i bash -c '{gbasf2_setup_command_str} > /dev/null && env'"
    )
    gbasf2_env_string = subprocess.run(
        echo_gbasf2_env_command, check=True, stdout=subprocess.PIPE, encoding="utf-8"
    ).stdout
    gbasf2_env = dict(line.split("=", 1) for line in gbasf2_env_string.splitlines())
    # The gbasf2 setup script on sets HOME to /ext/home/ueda if it's unset,
    # which later causes problems in the gb2_proxy_init subprocess. Therefore,
    # reset it to the caller's HOME.
    try:
        gbasf2_env["HOME"] = os.environ["HOME"]
    except KeyError:
        pass
    return gbasf2_env


def get_proxy_info():
    """Run ``gbasf2_proxy_info.py`` to retrieve a dict of the proxy status."""
    proxy_info_script_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "gbasf2_proxy_info.py"
    )

    # Setting ``ensure_proxy_initialized=False`` is vital here, otherwise we get
    # an infinite loop because run_with_gbasf2 will then check for the proxy info
    proc = run_with_gbasf2(
        [proxy_info_script_path],
        capture_output=True,
        ensure_proxy_initialized=False,
    )
    return json.loads(proc.stdout)


def get_dirac_user():
    """Get dirac user name."""
    # ensure proxy is initialized, because get_proxy_info can't do it, otherwise
    # it causes an infinite loop
    setup_dirac_proxy()
    try:
        return get_proxy_info()["username"]
    except KeyError as err:
        raise RuntimeError(
            "Could not obtain dirac user name from `gb2_proxy_init` output."
        ) from err


def setup_dirac_proxy():
    """Run ``gb2_proxy_init -g belle`` if there's no active dirac proxy. If there is, do nothing."""
    # first run script to check if proxy is already alive or needs to be initalized
    try:
        if get_proxy_info()["secondsLeft"] > 3600 * gbasf2_min_proxy_lifetime:
            return
    #  error is raised if proxy hasn't been initialized yet, in that case also process with initialization
    except subprocess.CalledProcessError:
        pass

    # initialize proxy
    lifetime = gbasf2_proxy_lifetime
    if not isinstance(lifetime, int) or lifetime <= 0:
        warnings.warn(
            "Setting 'gbasf2_proxy_lifetime' should be a positive integer.",
            RuntimeWarning,
        )
    hours = int(lifetime)
    proxy_init_cmd = shlex.split(f"gb2_proxy_init -g belle -v {hours}:00 --pwstdin")

    while True:
        pwd = getpass("Certificate password: ")
        try:
            proc = run_with_gbasf2(
                proxy_init_cmd,
                input=pwd,
                ensure_proxy_initialized=False,
                capture_output=True,
                check=True,
            )
        finally:
            del pwd
        # Check if there were any errors, since gb2_proxy_init often still exits without errorcode and sends messages to stdout
        out, err = proc.stdout, proc.stderr
        all_output = (
            out + err
        )  # gb2_proxy_init errors are usually in stdout, but for future-proofing also check stderr

        # if wrong password, retry password entry
        # usually the output then contains "Bad passphrase", but for future-proofing we check "bad pass"
        if "bad pass" in all_output.lower():
            print("Wrong certificate password, please try again.", file=sys.stderr)
            continue

        # for all other errors, raise an exception and abort
        # Usually for errors, the output contains the line: "Error: Operation not permitted ( 1 : )"
        if "error" in all_output.lower():
            raise subprocess.CalledProcessError(
                returncode=errno.EPERM,
                cmd=proxy_init_cmd,
                output=(
                    "There seems to be an error in the output of gb2_proxy_init."
                    f"\nCommand output:\n{out}"
                ),
            )
        # if no  wrong password and no other errors, stop loop and return
        return


def query_lpns(ds_query: str, dirac_user: Optional[str] = None) -> List[str]:
    """
    Query DIRAC for LPNs matching query, and return them as a list.
    This function exists to avoid manual string parsing of ``gb2_ds_list``.
    """
    if dirac_user is None:
        dirac_user = get_dirac_user()

    ds_list_script_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "gbasf2_ds_list.py"
    )

    query_cmd = [ds_list_script_path, "--dataset", ds_query, "--user", dirac_user]
    proc = run_with_gbasf2(
        query_cmd,
        capture_output=True,
        ensure_proxy_initialized=True,
    )

    lpns = json.loads(proc.stdout)
    if not isinstance(lpns, list):
        raise TypeError(
            f"Expected gbasf2 dataset query to return list, but instead the command\n{query_cmd}\n"
            + f"returned: {lpns}"
        )
    return lpns


def lfn_follows_gb2v5_convention(lfn: str) -> bool:
    """
    Check if the LFN follows the convention of gbasf2 release 5, i.e.
       <name>_<gbasf2param>_<jobID>_<rescheduleNum>.root
    Args:
        lfn: Logical file name, a file path on the grid
    """
    # adapted the logic from the BelleDirac function ``findDuplicatedJobID()``
    if len(lfn.split("_")) < 2 or "job" not in lfn.split("_")[-2]:
        return False
    return True


def _get_lfn_upto_reschedule_number(lfn: str) -> str:
    """
    Get a string of the gbasf2 v5 LFN upto the reschule number.
    E.g. if the LFN is ``<name>_<gbasf2param>_<jobID>_<rescheduleNum>.root``
    return ````<name>_<gbasf2param>_<jobID>``.
    """
    if not lfn_follows_gb2v5_convention(lfn):
        raise ValueError(
            "LFN does does not conform to the new gbasf2 v5 style, "
            "thus getting the substring upto the reschedule number does not make sense"
        )
    return "_".join(lfn.split("_")[:-1])


def get_unique_lfns(lfns: Iterable[str]) -> Set[str]:
    """
    From list of gbasf2 LFNs which include duplicate outputs for rescheduled
    jobs return filtered list which only include the LFNs for the jobs with the
    highest reschedule number.
    Gbasf2 v5 has outputs of the form
    ``<name>_<gbasf2param>_<jobID>_<rescheduleNum>.root``.  When using
    ``gb2_ds_list``, we see duplicates LFNs where all parts are the same accept
    the ``rescheduleNum``.  This function returns only those with the highest number.
    """
    # if dataset does not follow gbasf2 v5 convention, assume it was produced
    # with old release and does not contain duplicates
    if not all(lfn_follows_gb2v5_convention(lfn) for lfn in lfns):
        return set(lfns)
    # if it is of the gbasf v5 form, group the outputs by the substring upto the
    # reschedule number and return list of maximums of each group
    lfns = sorted(lfns, key=_get_lfn_upto_reschedule_number)
    return {
        max(lfn_group)
        for _, lfn_group in groupby(lfns, key=_get_lfn_upto_reschedule_number)
    }


# initialize submit command
BatchJob = Gbasf2Process(
    steering_file=steeringfile,
    gbasf2_dataset=gbasf2_dataset,
    release=release,
    sandbox_files=sandbox_input_files,
    maxtries=maxretries,
    outname=outname,
    skimfiles=output_filelist,
    download_log_files=download_logs,
)

if setProxy:
    timenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(proxy_text_file, "w+") as f:
        f.write(f"Proxy initialized at {timenow}.")
else:
    # submit job
    BatchJob.start_job()
    time.sleep(10)

    # check job status regularly
    while BatchJob.get_job_status() in ["RUN", "PEND"]:
        timenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Job {BatchJob.get_job_id()} still running at {timenow}")
        time.sleep(10)

    # raise error if job is not running anymore and not done
    if BatchJob.get_job_status() != "DONE":
        raise RuntimeError(
            f"ERROR: Job {BatchJob.get_job_id()} failed with status {BatchJob.get_job_status()}!"
        )
