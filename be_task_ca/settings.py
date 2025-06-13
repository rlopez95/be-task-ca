from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_uri = "postgresql://postgres:example@localhost:5432/postgres"


settings = Settings()
