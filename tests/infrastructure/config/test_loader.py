from __future__ import annotations

from pathlib import Path

import pytest

from aitradebot.infrastructure.config.exceptions import (
    ConfigurationFileNotFoundError,
)
from aitradebot.infrastructure.config.loader import ConfigLoader


def test_load_settings_success() -> None:
    """Configuration should load successfully."""

    settings = ConfigLoader.load(Path("config/settings.yaml"))

    assert settings.application.name == "AITradeBotV2"
    assert settings.market.timeframe == "2m"
    assert settings.broker.mode == "paper"


def test_missing_configuration_file() -> None:
    """Loading a missing configuration file should raise an exception."""

    with pytest.raises(ConfigurationFileNotFoundError):
        ConfigLoader.load(Path("config/does_not_exist.yaml"))