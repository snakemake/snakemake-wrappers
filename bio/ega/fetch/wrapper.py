from pathlib import Path
import shlex
import shutil
import subprocess as sp
import sys
import tempfile

if snakemake.log:
    sys.stderr = open(snakemake.log[0], "w")

fileid = snakemake.params.fileid

fmt = Path(snakemake.output[0]).suffix[1:].upper()

extra_pyega3 = shlex.split(snakemake.params.get("extra_pyega3", ""))
extra_fetch = shlex.split(snakemake.params.get("extra_fetch", ""))

with tempfile.TemporaryDirectory() as tmpdir:
    cmd = (
        ["pyega3"]
        + extra_pyega3
        + ["fetch", "--output-dir", tmpdir, "--format", fmt, fileid]
        + extra_fetch
    )
    sp.run(
        cmd,
        stdout=sys.stderr,
        stderr=sp.STDOUT,
        check=True,
    )
    # obtain path to the downloaded file (it should be the only file with that
    # extension in the temp dir)
    glob_res = list((Path(tmpdir) / fileid).glob(f"*.{fmt.lower()}"))
    assert (
        len(glob_res) == 1
    ), "bug: more than one file with desired extension downloaded by pyega3"

    # Move the file to the output
    shutil.move(glob_res[0], snakemake.output[0])
