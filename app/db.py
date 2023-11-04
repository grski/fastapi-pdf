import pugsql

from settings.base import settings

user_queries = pugsql.module("db/queries/users")
query_connection = user_queries.connect(settings.DATABASE_URL)
