from dataclasses import dataclass, field
from typing import Dict, Union
from pathlib import Path
import sys
from config.constants import (
    TRF_DEFAULT_PARAMS,
    TRF_DEFAULT_FLAGS_WITH_VALUE,
    TRF_DEFAULT_FLAGS_BOOL,
)
from utils.tee import Tee

@dataclass
class TRFConfig:
    # Default configuration for parameters, flags with value, and boolean flags
    params: Dict[str, str] = field(default_factory=lambda: TRF_DEFAULT_PARAMS.copy())
    flags_with_value: Dict[str, str] = field(default_factory=lambda: TRF_DEFAULT_FLAGS_WITH_VALUE.copy())
    flags_bool: Dict[str, bool] = field(default_factory=lambda: TRF_DEFAULT_FLAGS_BOOL.copy())
    log_file_path: Union[str, Path, None] = None

    def __post_init__(self):
        if self.log_file_path:
            log_file = open(str(self.log_file_path), "a")
            sys.stdout = Tee(sys.__stdout__, log_file)
            sys.stderr = Tee(sys.__stderr__, log_file)

    def update_params(self, user_params: Dict[str, str]) -> None:
        """
        Directly updates TRF numeric params with pre-validated user values.
        """
        normalized = {k.lower(): v for k, v in user_params.items()}
        self.params.update(normalized)
        print(f"param: {self.params}")

    def update_flags_bool(self, user_flags: Dict[str, bool]) -> None:
        """
        Updates boolean flags (like `-m`, `-f`, etc.) from pre-parsed user input.
        Also applies TRF-specific logic (e.g. -h implies -d).
        """
        if user_flags:
            normalized = {k.lstrip('-').lower(): v for k, v in user_flags.items()}
            self.flags_bool = normalized  # Override defaults if any user flag is given
        else:
            self.flags_bool = TRF_DEFAULT_FLAGS_BOOL.copy()

        # TRF logic: -h (suppress HTML) implies -d (data file)
        if self.flags_bool.get("h", False):
            self.flags_bool["d"] = True

        print(f"param: {self.flags_bool}")

    def update_flags_with_value(self, user_flags: Dict[str, str]) -> None:
        """
        Updates flags that require values (e.g., `-l 2`) from pre-parsed input.
        """
        normalized = {k.lstrip('-').lower(): v for k, v in user_flags.items()}
        self.flags_with_value.update(normalized)
        print(f"param: {self.flags_with_value}")

    def build_command(self, input_file: str) -> str:
        """
        Builds the final TRF command-line string.
        """
        param_str = " ".join(f"{value}" for key, value in self.params.items())
        flags_bool_str = " ".join(f"-{flag}" for flag, enabled in self.flags_bool.items() if enabled)
        flags_with_value_str = " ".join(f"-{flag} {value}" for flag, value in self.flags_with_value.items())

        return f"trf {input_file} {param_str} {flags_bool_str} {flags_with_value_str}"
