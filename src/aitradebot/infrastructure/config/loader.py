from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import ValidationError

from aitradebot.infrastructure.config.exceptions import (
    ConfigurationFileNotFoundError,
    ConfigurationValidationError,
)
from aitradebot.infrastructure.config.models import Settings
class ConfigLoader:
    """Loads application configuration from YAML."""

    @staticmethod
    def load(config_path: Path) -> Settings:
        """
        Load application settings from a YAML file.
        """
        if not config_path.exists():
            raise ConfigurationFileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with config_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        try:
            return Settings.model_validate(data)
        except ValidationError as exc:
            raise ConfigurationValidationError(str(exc)) from exc