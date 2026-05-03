"""libarchive compression.

Enables archive compression for various formats (zip, 7zip, tar, etc) across platforms.
"""

__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2026, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

import sys
from pathlib import Path, PurePosixPath

import libarchive


def _listify(x: str | list | None) -> list | None:
    if isinstance(x, str):
        x = [x]
    return x


def _validate_input_file(path: Path) -> None:
    """Reject invalid input paths."""
    if not path.is_file():
        raise ValueError(f"Input file {path!r} is invalid.")


def _validate_internal_path(path: str) -> None:
    """Reject archive paths that would be unsafe or ambiguous."""
    parsed = PurePosixPath(path)
    if (
        not path
        or path.endswith("/")
        or parsed.is_absolute()
        or any(part in {"", ".", ".."} for part in parsed.parts)
    ):
        raise ValueError(f"Internal path {path!r} is invalid.")


def compress(
    archive_path: Path | str,
    input_files: list[Path | str],
    format_name: str,
    filter_name: str,
    internal_paths: list[str] | None = None,
    **kwargs,
) -> None:
    """Create an archive containing the given files.

    Args:
        archive_path: Path where the archive should be created.
        input_files: Files to add to the archive.
        format_name: libarchive format name ("zip", "pax", "7zip", "gnutar", "ustar", etc).
        filter_name: libarchive compression filter name ("gzip", "xz", "zstd", etc).
        internal_paths: Optional archive-internal paths for the input files.
            If provided, must have the same length as input_files.

    """
    archive_path = Path(archive_path)
    input_files = [Path(path) for path in input_files]
    if internal_paths is None:
        internal_paths = [path.name for path in input_files]

    if len(input_files) != len(internal_paths):
        raise ValueError("Input files and internal paths must have the same length.")
    if len(set(internal_paths)) != len(internal_paths):
        raise ValueError("Internal paths must not contain duplicates.")

    created = False
    try:
        with libarchive.file_writer(
            str(archive_path),
            format_name,
            filter_name=filter_name,
            **kwargs,
        ) as archive:
            created = True
            for input_path, archive_name in zip(
                input_files, internal_paths, strict=True
            ):
                _validate_input_file(input_path)
                _validate_internal_path(archive_name)
                archive.add_file(
                    str(input_path),
                    pathname=archive_name,
                )
    except Exception:
        if created:
            archive_path.unlink(missing_ok=True)
        raise


def main():
    """Main snakemake process."""
    sys.stderr = open(snakemake.log[0], "w", buffering=1)

    compress(
        archive_path=snakemake.output.archive,
        input_files=_listify(snakemake.input),
        format_name=snakemake.params.format_name,
        filter_name=snakemake.params.get("filter_name", None),
        internal_paths=_listify(snakemake.params.get("internal_paths", None)),
        **snakemake.params.get("extras", {}),
    )


if __name__ == "__main__":
    main()
