from __future__ import annotations


class ConfigurationError(Exception):
    """Base exception for configuration errors."""


class ConfigurationFileNotFoundError(ConfigurationError):
    """Raised when the configuration file cannot be found."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when the configuration is invalid."""
