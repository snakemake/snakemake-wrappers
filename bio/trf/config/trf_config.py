"""
This module provides default constants and the `TRFConfig` class for configuring
Tandem Repeat Finder (TRF) command-line arguments.

It defines parameters, boolean flags, and flags with values for TRF configuration.
The `TRFConfig` class allows users to update and build the final TRF command with user inputs.

Constants:
- `TRF_DEFAULT_PARAMS`: A dictionary of default numeric parameters for TRF.
- `TRF_DEFAULT_FLAGS_WITH_VALUE`: A dictionary of default flags that require a value.
- `TRF_DEFAULT_FLAGS_BOOL`: A dictionary of default boolean flags for TRF.

Classes:
- `TRFConfig`: A class that manages TRF configuration, allowing updates and command generation.
"""

import copy
from dataclasses import dataclass, field
from typing import Dict

from config.constants import (
    TRF_DEFAULT_FLAGS_BOOL,
    TRF_DEFAULT_FLAGS_WITH_VALUE,
    TRF_DEFAULT_PARAMS,
)


@dataclass
class TRFConfig:
    """
    TRFConfig class for managing TRF configuration.

    This class allows for updating parameters, boolean flags, and flags with values
    used in constructing the TRF command. It helps to build the final TRF command
    based on user-specified options or set defaults.

    Attributes:
        params (Dict[str, str]): A dictionary of numeric parameters for TRF.
        flags_with_value (Dict[str, str]): A dictionary of flags that require values.
        flags_bool (Dict[str, bool]): A dictionary of boolean flags for TRF.

    Methods:
        update_params(user_params):
            Updates the numeric parameters for TRF with user-provided values.

        update_flags_bool(user_flags):
            Updates the boolean flags for TRF based on user input.

        update_flags_with_value(user_flags):
            Updates flags that require values (e.g., `-l 2`) with user-specified values.

        build_command(input_file):
            Builds the final TRF command-line string based on the real time configuration.
    """

    params: Dict[str, str] = field(
        default_factory=lambda: copy.deepcopy(TRF_DEFAULT_PARAMS)
    )  # noqa: W0108
    flags_with_value: Dict[str, str] = field(default_factory=dict)
    flags_bool: Dict[str, bool] = field(default_factory=dict)

    def update_params(self, user_params: Dict[str, str]) -> None:
        """
        Update the numeric parameters for TRF with user-provided values.

        This method takes a dictionary of parameters and updates the `params` attribute
        by normalizing the keys to lowercase.

        Args:
            user_params (Dict[str, str]): A dictionary of user-specified numeric parameters.

        Returns:
            None
        """
        normalized = {k.lower(): v for k, v in user_params.items()}
        self.params.update(normalized)

    def update_flags_bool(self, user_flags: Dict[str, bool]) -> None:
        """
        Update the boolean flags for TRF with user-provided values.

        This method updates the `flags_bool` dictionary based on the provided flags.

        Args:
            user_flags (Dict[str, bool]): A dictionary of boolean flags where keys are
                                          flag names (e.g., `m`, `f`) and values are
                                          True/False.

        Returns:
            None
        """
        if user_flags:
            normalized = {k.lstrip("-").lower(): v for k, v in user_flags.items()}
            self.flags_bool = normalized

    def update_flags_with_value(self, user_flags: Dict[str, str]) -> None:
        """
        Update the flags that require values (e.g., `-l 2`) with user-provided values.

        This method updates the `flags_with_value` dictionary by normalizing the flag
        names and applying the user-specified values.

        Args:
            user_flags (Dict[str, str]): A dictionary of flags that require values
                                         (e.g., `-l 2`, where `l` is the flag and `2` is the value).

        Returns:
            None
        """
        if user_flags:
            normalized = {k.lstrip("-").lower(): v for k, v in user_flags.items()}
            self.flags_with_value.update(normalized)

    def build_command(self, input_file: str) -> str:
        """
        Build the final TRF command string.

        This method generates the full command-line string for running TRF based on
        the runtime configuration (params, flags, and flags with values).

        Args:
            input_file (str): The path to the input file (e.g., a FASTA file).

        Returns:
            str: The complete TRF command string.
        """
        if not self.flags_with_value and not self.flags_bool:
            self.flags_with_value = copy.deepcopy(TRF_DEFAULT_FLAGS_WITH_VALUE)
            self.flags_bool = copy.deepcopy(TRF_DEFAULT_FLAGS_BOOL)

        print(f"{self.flags_bool} , {self.flags_with_value}")
        param_str = " ".join(f"{value}" for key, value in self.params.items())
        flags_bool_str = " ".join(
            f"-{flag}" for flag, enabled in self.flags_bool.items() if enabled
        )
        flags_with_value_str = " ".join(
            f"-{flag} {value}" for flag, value in self.flags_with_value.items()
        )

        return f"trf {input_file} {param_str} {flags_bool_str} {flags_with_value_str}"
