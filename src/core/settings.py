import secrets
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    db_url: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    secret_key: str = secrets.token_hex(32)

    @property
    def db_url(self) -> str:
        return self.db_url.format(
            db_user=self.db_user,
            db_password=self.db_password,
            db_host=self.db_host,
            db_port=self.db_port,
            db_name=self.db_name,
        )


@lru_cache(typed=True)
def load_settings() -> Settings:
    return Settings()
