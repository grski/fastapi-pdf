from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "business-assistant-api"
    DOMAIN: str = Field(env="DOMAIN", default="aisays.pl")
    ENVIRONMENT: str = Field(env="ENVIRONMENT", default="local")
    SENTRY_DSN: str = Field(env="SENTRY_DSN", default="None")

    DB_ENDPOINT: str = Field(env="DB_ENDPOINT")
    DB_PORT: int = Field(env="DB_PORT")
    DB_PASSWORD: str = Field(env="DB_PASSWORD")
    DB_USERNAME: str = Field(env="DB_USERNAME")
    DB_NAME: str = Field(env="DB_NAME")

    DATABASE_URL: str = Field(env="DATABASE_URL", default="None")

    TIMEOUT: int = Field(env="TIMEOUT", default=120)
    WORKERS: int = Field(env="NUMBER_OF_WORKER_LOCALS", default=2)
    RELOAD: bool = Field(env="RELOAD", default=False)

    SENDGRID_API_KEY: str = Field(env="SENDGRID_API_KEY")
    EMAIL_FROM: str = Field(env="EMAIL_FROM")

    OPENAI_API_KEY: str = Field(env="OPENAI_API_KEY", default="None")
    INVITE_KEY_URL: str = Field(env="INVITE_KEY_URL")

    APP_ENTRYPOINT: str = Field(env="APP_ENTRYPOINT", default="localhost")
    CORS_ORIGINS: str = Field(env="CORS_ORIGINS", default="localhost")

    STRIPE_API_KEY: str = Field(env="STRIPE_API_KEY", default="None")
    STRIPE_WEBHOOK_SECRET: str = Field(env="STRIPE_WEBHOOK_SECRET", default="None")

    class Config:
        env_file = ".env"

    @property
    def cors_allowed_origins(self):
        return self.CORS_ORIGINS.split(",")


settings = Settings()
