import pugsql

from settings.base import settings

DATABASE_URI = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_ENDPOINT}:{settings.DB_PORT}/{settings.DB_NAME}"
ASYNC_DATABASE_URI: str = f"postgresql+asyncpg://{DATABASE_URI}"

user_queries = pugsql.module("db/queries/users")
query_connection = user_queries.connect(settings.DATABASE_URL)
