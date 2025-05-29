import pytest
import sys
from pathlib import Path
import os


from utils.log_utils import log_output_dir_contents


def test_empty_output_dir_logs_warning(tmp_path, capsys):
    # Setup: create empty output directory and log file path
    output_dir = tmp_path / "empty_output"
    output_dir.mkdir()
    log_file = tmp_path / "log.txt"

    # Act: run your logging function
    log_output_dir_contents(str(output_dir), str(log_file))

    # Capture stdout (printed output)
    captured = capsys.readouterr()

    # Assert: verify the output contains the warning message
    expected_msg = f"No output files found in '{output_dir}'. TRF may have failed or produced no output."
    assert expected_msg in captured.out
    
    with open(log_file) as f:
        assert expected_msg in f.read()
