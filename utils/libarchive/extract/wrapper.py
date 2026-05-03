"""libarchive wrapper.

Enables archive decompression for various formats (zip, 7zip, tar, etc) across platforms.
"""

__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2026, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

import sys
from pathlib import Path

import libarchive


def _listify(x: str | list) -> list:
    if isinstance(x, str):
        x = [x]
    return x


def extract(
    archive_file: str,
    internal_paths: list[str],
    output_files: list[str],
) -> None:
    """Extract archive members to exact output paths.

    Each output path is treated as the final filename, not a directory.
    """
    if len(internal_paths) != len(output_files):
        raise ValueError(
            "Requested files and output locations must be of the same length."
        )
    if len(set(internal_paths)) != len(internal_paths):
        raise ValueError("Requested files must not contain duplicates.")
    if len(set(output_files)) != len(output_files):
        raise ValueError("Requested output files must not contain duplicates.")

    output_mapping = {
        file: Path(output_file)
        for file, output_file in zip(internal_paths, output_files)
    }

    requested = set(output_mapping)
    found: set[str] = set()
    created_paths: set[Path] = set()

    try:
        with libarchive.file_reader(archive_file) as archive:
            for entry in archive:
                name = entry.pathname

                if name not in requested:
                    continue

                if name in found:
                    raise ValueError(
                        f"Archive contains ambiguous duplicate member: {name!r}"
                    )

                if not entry.isfile:
                    raise ValueError(f"Error: {name!r} is not a regular file.")

                output_path = output_mapping[name]
                output_path.parent.mkdir(parents=True, exist_ok=True)

                with output_path.open("xb") as dst:
                    created_paths.add(output_path)

                    for block in entry.get_blocks():
                        dst.write(block)

                found.add(name)

        missing = sorted(requested - found)
        if missing:
            raise ValueError(f"Error: {missing!r} not found in archive.")
    except Exception:
        # Remove all files created by this call
        for path in created_paths:
            path.unlink(missing_ok=True)
        raise


def main():
    """Main snakemake process."""
    sys.stderr = open(snakemake.log[0], "w", buffering=1)

    extract(
        archive_file=snakemake.input.archive,
        internal_paths=_listify(snakemake.params.internal_paths),
        output_files=_listify(snakemake.output),
    )


if __name__ == "__main__":
    main()
