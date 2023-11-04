from pydantic import Field
from pydantic_settings import BaseSettings

from settings.base import settings

THREADS_PER_CORE = 2
DEFAULT_NUMBER_OF_WORKERS_ON_LOCAL = 1


def calculate_workers():
    if settings.is_local:
        return DEFAULT_NUMBER_OF_WORKERS_ON_LOCAL

    import multiprocessing

    # for cpus with two threads per core this is the recommended formula
    # we might want to adjust this for our use case and infrastructure in the future
    # as in general one vcpu in aws is not the same as one cpu core in a physical machine
    # usually one vcpu is one thread of a cpu core, for starters it's good enough though

    return multiprocessing.cpu_count() * THREADS_PER_CORE + 1


# config = GunicornConfig()
bind = "0.0.0.0:8000"
workers = settings.WORKERS
worker_class = "uvicorn.workers.UvicornWorker"
timeout = settings.TIMEOUT
reload = settings.RELOAD
