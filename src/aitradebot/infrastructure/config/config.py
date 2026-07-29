from __future__ import annotations

from pathlib import Path

from aitradebot.infrastructure.config.loader import ConfigLoader
from aitradebot.infrastructure.config.models import Settings


def load_settings() -> Settings:
    """
    Load the application's settings from the default configuration file.
    """
    config_path = Path("config/settings.yaml")
    return ConfigLoader.load(config_path)
