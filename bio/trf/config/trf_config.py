from dataclasses import dataclass, field
from typing import Dict
from config.constants import (
    TRF_DEFAULT_PARAMS,
    TRF_DEFAULT_FLAGS_WITH_VALUE,
    TRF_DEFAULT_FLAGS_BOOL,
)

@dataclass
class TRFConfig:
    # Default configuration for parameters, flags with value, and boolean flags
    params: Dict[str, str] = field(default_factory=lambda: TRF_DEFAULT_PARAMS.copy())
    flags_with_value: Dict[str, str] = field(default_factory=lambda: TRF_DEFAULT_FLAGS_WITH_VALUE.copy())
    flags_bool: Dict[str, bool] = field(default_factory=lambda: TRF_DEFAULT_FLAGS_BOOL.copy())

    def update_params(self, user_params: Dict[str, str]) -> None:
        """
        Directly updates TRF numeric params with pre-validated user values.
        """
        normalized = {k.lower(): v for k, v in user_params.items()}
        self.params.update(normalized)

    def update_flags_bool(self, user_flags: Dict[str, bool]) -> None:
        """
        Updates boolean flags (like `-m`, `-f`, etc.) from pre-parsed user input.
        Also applies TRF-specific logic (e.g. -h implies -d).
        """
        normalized = {k.lstrip('-').lower(): v for k, v in user_flags.items()}
        self.flags_bool.update(normalized)

        # TRF logic: -h (suppress HTML) implies -d (data file)
        if self.flags_bool.get("h", False):
            self.flags_bool["d"] = True

    def update_flags_with_value(self, user_flags: Dict[str, str]) -> None:
        """
        Updates flags that require values (e.g., `-l 2`) from pre-parsed input.
        """
        normalized = {k.lstrip('-').lower(): v for k, v in user_flags.items()}
        self.flags_with_value.update(normalized)

    def build_command(self, input_file: str) -> str:
        """
        Builds the final TRF command-line string.
        """
        param_str = " ".join(f"{value}" for key, value in self.params.items())
        flags_bool_str = " ".join(f"-{flag}" for flag, enabled in self.flags_bool.items() if enabled)
        flags_with_value_str = " ".join(f"-{flag} {value}" for flag, value in self.flags_with_value.items())

        return f"trf {input_file} {param_str} {flags_bool_str} {flags_with_value_str}"

