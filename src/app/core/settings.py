from __future__ import annotations

from configparser import ConfigParser
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[2]
CONFIG_DIR = ROOT_DIR / "config"


class Settings(BaseSettings):
    """
    Application settings.

    Environment variables override values loaded from app.ini.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = Field(default="Financial Health Engine")
    app_version: str = Field(default="0.1.0")
    environment: str = Field(default="development")

    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)

    api_key: str = Field(default="change-me")
    api_key_header: str = Field(default="X-API-Key")

    log_level: str = Field(default="INFO")


@lru_cache
def get_settings() -> Settings:
    parser = ConfigParser()

    parser.read(CONFIG_DIR / "app.ini")

    settings = Settings()

    if parser.has_section("application"):
        settings.app_name = parser["application"].get("name", settings.app_name)
        settings.app_version = parser["application"].get(
            "version",
            settings.app_version,
        )
        settings.environment = parser["application"].get(
            "environment",
            settings.environment,
        )

    if parser.has_section("server"):
        settings.host = parser["server"].get("host", settings.host)
        settings.port = parser["server"].getint("port", settings.port)

    if parser.has_section("security"):
        settings.api_key_header = parser["security"].get(
            "api_key_header",
            settings.api_key_header,
        )

    return settings


settings = get_settings()