from fastapi import FastAPI

from app import version
from app.core.api import router as core_router
from app.core.logs import logger
from app.core.middlewares import apply_middlewares
from app.stripe.api import router as stripe_router
from app.users.api import router as users_router

app = FastAPI(version=version)
app = apply_middlewares(app)


app.include_router(core_router)
app.include_router(stripe_router)
app.include_router(users_router)
logger.info("App is ready!")
