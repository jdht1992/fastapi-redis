from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    LEADERBOARD_REDIS_CHANNEL: str

    model_config: dict = SettingsConfigDict(
        env_file=".env"
    )


@lru_cache
def get_settings():
    return ConfigSettings()


settings = get_settings()
