import os

import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
    version = data["tool"]["poetry"]["version"]

if os.environ.get("ENVIRONMENT", "local") == "local":
    from dotenv import load_dotenv

    load_dotenv()
