import threading
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api.route.router import v1_router
from src.config.config import settings
from src.redis_config.redis import RedisBroker


@asynccontextmanager
async def lifespan(app: FastAPI):
    thread = threading.Thread(
        target=RedisBroker().consume, args={settings.LEADERBOARD_REDIS_CHANNEL}
    )
    thread.start()  # Keeps the thread running as long as FastAPI app is running
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(v1_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
