from pathlib import Path
import sys
import warnings
import traceback
from typing import Union
from utils.tee import Tee  # Import shared Tee class


def log_output_dir_contents(output_dir: Union[str, Path], log_file_path:  Union[str, Path]) -> None:
    """
    Logs and prints the contents of the specified output directory.

    This function:
    - Lists all files in the output directory.
    - Prints file names and sizes to stdout.
    - Duplicates all stdout and stderr output to the specified log file.
    - Handles empty directories gracefully with an informative message.

    Parameters:
    - output_dir (str): Path to the directory whose contents should be logged.
    - log_file_path (str | Path): Path to the log file.

    Returns:
    - None
    """

    if log_file_path is not None:
        log_file_path = Path(log_file_path)
    
    if output_dir is not None:
        output_dir = Path(output_dir)

    with open(log_file_path, 'a') as log_file:
        sys.stdout = Tee(sys.__stdout__, log_file)
        sys.stderr = Tee(sys.__stderr__, log_file)

        try:
            output_files = sorted(output_dir.iterdir()) if output_dir.exists() else []

            if not output_files:
                msg = f"No output files found in '{output_dir}'. TRF may have failed or produced no output."
                print(msg)
                warnings.warn(msg)
            else:
                print(f"TRF output directory '{output_dir}' contains {len(output_files)} files:")
                for file in output_files:
                    file_info = f"  - {file.name} ({file.stat().st_size} bytes)"
                    print(file_info)

        except Exception:
            print("An unexpected error occurred during output directory logging:")
            traceback.print_exc()

        finally:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
