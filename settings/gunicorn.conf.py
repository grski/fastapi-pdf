from pydantic import Field
from pydantic_settings import BaseSettings

from settings.base import settings

THREADS_PER_CORE = 2


def calculate_workers():
    import multiprocessing

    # for cpus with two threads per core this is the recommended formula
    # we might want to adjust this for our use case and infrastructure in the future
    # as in general one vcpu in aws is not the same as one cpu core in a physical machine
    # usually one vcpu is one thread of a cpu core, for starters it's good enough though
    return multiprocessing.cpu_count() * THREADS_PER_CORE + 1


class GunicornConfig(BaseSettings):
    TIMEOUT: int = Field(env="TIMEOUT", default=120)
    WORKERS: int = Field(env="NUMBER_OF_WORKER_LOCALS", default=2)
    RELOAD: bool = Field(env="RELOAD", default=False)

    class Config:
        env_file = ".env"


# config = GunicornConfig()
bind = "0.0.0.0:8000"
workers = settings.WORKERS
worker_class = "uvicorn.workers.UvicornWorker"
timeout = settings.TIMEOUT
reload = settings.RELOAD
