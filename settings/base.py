from pydantic import Field
from pydantic_settings import BaseSettings

from app.core.constants import EnvironmentsEnum


class Settings(BaseSettings):
    APP_NAME: str = "business-assistant-api"
    ENVIRONMENT: EnvironmentsEnum = Field(env="ENVIRONMENT", default=EnvironmentsEnum.LOCAL)
    SENTRY_DSN: str = Field(env="SENTRY_DSN", default="")

    DATABASE_URL: str = Field(env="DATABASE_URL")

    TIMEOUT: int = Field(env="TIMEOUT", default=120)
    WORKERS: int = Field(env="NUMBER_OF_WORKER_LOCALS", default=2)
    RELOAD: bool = Field(env="RELOAD", default=False)

    SENDGRID_API_KEY: str = Field(env="SENDGRID_API_KEY")
    EMAIL_FROM: str = Field(env="EMAIL_FROM")

    API_ENTRYPOINT: str = Field(env="API_ENTRYPOINT", default="http://localhost:8000")
    APP_ENTRYPOINT: str = Field(env="APP_ENTRYPOINT", default="http://localhost")
    CORS_ORIGINS: str = Field(env="CORS_ORIGINS", default="localhost")

    STRIPE_API_KEY: str = Field(env="STRIPE_API_KEY", default="")
    STRIPE_WEBHOOK_SECRET: str = Field(env="STRIPE_WEBHOOK_SECRET", default="")

    class Config:
        env_file = ".env"

    @property
    def cors_allowed_origins(self):
        return self.CORS_ORIGINS.split(",")


settings = Settings()
