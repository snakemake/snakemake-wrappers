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

    # Move the file to the output
    shutil.move(Path(tmpdir).glob(f"*.{fmt.lower()}"), snakemake.output[0])
