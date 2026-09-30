from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.core.config import settings


app = FastAPI(
    title="Dropbox Smart Desk",
    version="1.0.0",
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.session_secret,
    https_only=False,
)