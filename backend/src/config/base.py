from dataclasses import dataclass

from src.config.env import env


@dataclass(frozen=True)
class Config:
    """Configuration class to hold environment variables."""

    GOOGLE_CLIENT_ID: str = env.str("GOOGLE_CLIENT_ID", default="")
    GOOGLE_CLIENT_SECRET: str = env.str("GOOGLE_CLIENT_SECRET", default="")


config = Config()
