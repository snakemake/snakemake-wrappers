import os
import json
import urllib.request

from snakemake.shell import shell


def exception_to_log(check, msg):
    log = snakemake.log_fmt_shell(stdout=True, stderr=True)
    if not check:
        shell(f"""echo "{msg}" {log} """)
        # exit without stack trace
        os._exit(1)


def download_encff(accession, layout, dest):
    exception_to_log(
        check=accession.startswith("ENCFF"),
        msg=f"""Can't download accession "{accession}" directly as it isn't a file. This shouldn't happen..""",
    )
    url = f"https://www.encodeproject.org/files/{accession}/?format=json"
    try:
        response = urllib.request.urlopen(urllib.request.Request(url)).read()
    except urllib.error.HTTPError:
        exception_to_log(
            check=False,
            msg=f"""Having trouble connecting to ENCODE or the accesion "{accession}" doesn't exist.""",
        )
    response = json.loads(response.decode("utf-8"))

    exception_to_log(
        check=response["file_format"] == "fastq",
        msg=f"""Can't download accession "{accession}" directly as it doesn't refer to a fastq file. It is a "{response["file_format"]}" file.""",
    )

    exception_to_log(
        check=layout in ["single", "paired"],
        msg=f"""The layout of the sample is not single ended or paired, but it is "{layout}".""",
    )

    if layout == "single":
        url = "https://www.encodeproject.org" + response["href"]
        shell(f"wget -O - -o /dev/null {url} >> {dest.r1}")
    if layout == "paired":
        # lookup the mate
        mate_accession = response["paired_with"].split("/")[2]
        mate_url = f"https://www.encodeproject.org/files/{mate_accession}/?format=json"
        mate_response = json.loads(
            urllib.request.urlopen(urllib.request.Request(mate_url))
            .read()
            .decode("utf-8")
        )

        # get the urls to download them
        url = "https://www.encodeproject.org" + response["href"]
        mate_url = "https://www.encodeproject.org" + mate_response["href"]

        # if the mate is actually R1, swap them so that R1 always corresponds
        if response["paired_end"] == "2":
            url, mate_url = mate_url, url

        shell(f"wget -O - -o /dev/null {url} >> {dest.r1}")
        shell(f"wget -O - -o /dev/null {mate_url} >> {dest.r2}")


def download_encsr(accession, layout, dest):
    url = f"https://www.encodeproject.org/search/?type=File&dataset=/experiments/{accession}/&file_format=fastq&format=json&frame=object"
    try:
        response = urllib.request.urlopen(urllib.request.Request(url)).read()
    except urllib.error.HTTPError:
        exception_to_log(
            check=False,
            msg=f"""Having trouble connecting to ENCODE or the accesion "{accession}" doesn't exist.""",
        )
    response = json.loads(response.decode("utf-8"))

    # check if all run types are the same
    exception_to_log(
        check=len(set([file["run_type"] for file in response["@graph"]])) == 1,
        msg=f"""Not all the runs of "{accession} are of the same type: {set([file["run_type"] for file in response["@graph"]])}. It is ambiguous how to proceed.""",
    )
    inferred_layout = response["@graph"][0]["run_type"]

    if layout == "single":
        exception_to_log(
            check=inferred_layout == "single-ended",
            msg=f"""The sample was automatically inferred to be single-ended, but it is: "{inferred_layout}".""",
        )
        for encff_accession in response["@graph"]:
            encff_accession = encff_accession["accession"]
            download_encff(encff_accession, layout, dest)
    elif layout == "paired":
        exception_to_log(
            check=inferred_layout == "paired-ended",
            msg=f"""The sample was automatically inferred to be paired-ended, but it is: "{inferred_layout}".""",
        )

        # get all the R1s
        runs = [x["accession"] for x in response["@graph"] if x["paired_end"] == "1"]

        for run in runs:
            download_encff(run, layout, dest)
    else:
        assert False


# determine the layout (single-ended vs paired-ended)
exception_to_log(
    check=len(snakemake.output) in [1, 2],
    msg=f"""The numer of specified outputs of this rule should be 1 or 2, but it is "{len(snakemake.output)}".""",
)
if len(snakemake.output) == 1:
    layout = "single"
    exception_to_log(
        check=hasattr(snakemake.output, "r1"),
        msg=f"""Single-ended data needs to specify its output with r1.""",
    )
else:
    layout = "paired"
    exception_to_log(
        check=hasattr(snakemake.output, "r1") and hasattr(snakemake.output, "r2"),
        msg=f"""Paired-ended data needs to specify its output with r1 and r2.""",
    )

exception_to_log(
    check=snakemake.wildcards.accession.startswith(("ENCFF", "ENCSR")),
    msg=f"""The sample accession ({snakemake.wildcards.accession}) should start with ENCFF or ENCSR.""",
)
if snakemake.wildcards.accession.startswith("ENCFF"):
    download_encff(
        accession=snakemake.wildcards.accession, layout=layout, dest=snakemake.output
    )
else:
    download_encsr(
        accession=snakemake.wildcards.accession, layout=layout, dest=snakemake.output
    )
