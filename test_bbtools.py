import subprocess
import os
import tempfile
import shutil
import pytest
import sys
import yaml
from itertools import chain



class Skipped(Exception):
    pass


skip_if_not_modified = pytest.mark.xfail(raises=Skipped)


def run(wrapper, cmd, check_log=None):
    origdir = os.getcwd()
    with tempfile.TemporaryDirectory() as d:
        dst = os.path.join(d, "master")
        os.makedirs(dst, exist_ok=True)
        copy = lambda pth, src: shutil.copy(
            os.path.join(pth, src), os.path.join(dst, pth)
        )

        used_wrappers = []
        wrapper_file = "used_wrappers.yaml"
        if os.path.exists(os.path.join(wrapper, wrapper_file)):
            # is meta wrapper
            with open(os.path.join(wrapper, wrapper_file), "r") as wf:
                wf = yaml.load(wf, Loader=yaml.BaseLoader)
                used_wrappers = wf["wrappers"]
        else:
            used_wrappers.append(wrapper)

        for w in used_wrappers:
            success = False
            for ext in ("py", "R", "Rmd"):
                script = "wrapper." + ext
                if os.path.exists(os.path.join(w, script)):
                    os.makedirs(os.path.join(dst, w), exist_ok=True)
                    copy(w, script)
                    success = True
                    break
            assert success, "No wrapper script found for {}".format(w)
            copy(w, "environment.yaml")



        testdir = os.path.join(d, "test")
        # pkgdir = os.path.join(d, "pkgs")
        shutil.copytree(os.path.join(wrapper, "test"), testdir)
        # prepare conda package dir
        # os.makedirs(pkgdir)
        # switch to test directory
        os.chdir(testdir)
        if os.path.exists(".snakemake"):
            shutil.rmtree(".snakemake")
        cmd = cmd + [
            "--wrapper-prefix",
            "file://{}/".format(d),
            "--printshellcmds",
            "--show-failed-logs",
            "--conda-prefix",
            "/Users/silas/Downloads/condaenvs"
        ]



        # env = dict(os.environ)
        # env["CONDA_PKGS_DIRS"] = pkgdir
        try:
            subprocess.check_call(cmd)
        except Exception as e:
            # go back to original directory
            os.chdir(origdir)
            logfiles = [
                os.path.join(d, f)
                for d, _, files in os.walk(os.path.join(testdir, "logs"))
                for f in files
            ]
            for path in logfiles:
                with open(path) as f:
                    msg = "###### Logfile: " + path + " ######"
                    print(msg, "\n")
                    print(f.read())
                    print("#" * len(msg))
            if check_log is not None:
                for f in logfiles:
                    check_log(open(f).read())
            else:
                raise e
        finally:

            # go back to original directory
            os.chdir(origdir)


@skip_if_not_modified
def test_bbtools_pe():
    run(
        "bio/bbtools",
        [
            "snakemake",
            "--cores",
            "2",
            "--use-conda",
            "-F",
        ],
    )


@skip_if_not_modified
def test_bbtools_se():
    run(
        "bio/bbtools",
        [
            "snakemake",
            "--cores",
            "2",
            "--config",
            "reads_are_paired=False",
            "--use-conda",
            "-F",
        ],
    )


test_bbtools_pe()
test_bbtools_se()