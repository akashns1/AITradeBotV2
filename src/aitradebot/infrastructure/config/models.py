from __future__ import annotations

from pydantic import BaseModel


class ApplicationConfig(BaseModel):
    """Application configuration."""

    name: str
    version: str


class MarketConfig(BaseModel):
    """Market configuration."""

    timeframe: str


class RiskConfig(BaseModel):
    """Risk configuration."""

    max_risk_percent: float


class BrokerConfig(BaseModel):
    """Broker configuration."""

    mode: str


class LoggingConfig(BaseModel):
    """Logging configuration."""

    level: str


class Settings(BaseModel):
    """Root application settings."""

    application: ApplicationConfig
    market: MarketConfig
    risk: RiskConfig
    broker: BrokerConfig
    logging: LoggingConfig