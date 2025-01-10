# Code inside router.py
from fastapi import APIRouter

from src.api.v1 import leaderboard

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(leaderboard.router, tags=["Redis Leaderboard API"])
