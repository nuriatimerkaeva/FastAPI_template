import secrets
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        case_sensitive=False
    )
    DB_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    SECRET_KEY: str = secrets.token_hex(32)

    @property
    def db_url(self) -> str:
        return self.DB_URL.format(
            db_user=self.DB_USER,
            db_password=self.DB_PASSWORD,
            db_host=self.DB_HOST,
            db_port=self.DB_PORT,
            db_name=self.DB_NAME,
        )


@lru_cache(typed=True)
def load_settings() -> Settings:
    return Settings()


