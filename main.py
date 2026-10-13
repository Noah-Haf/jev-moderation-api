"""Main.py - Initialise FastAPI application and attach router(s)."""

from fastapi import FastAPI

from routers.text import textRouter

app = FastAPI()

app.include_router(textRouter)
