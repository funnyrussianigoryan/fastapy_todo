from contextlib import asynccontextmanager

from fastapi import FastAPI
from databases import Database
from src.api import include_routers
from src.core.settings import get_settings
import src.controller.todo as todo_module

config = get_settings()

db = Database(config.db.dsn)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.connect()
    todo_module.todo_controller = todo_module.TodoController(db)
    yield
    await db.disconnect()


app = FastAPI(title="FastAPI - todo list", lifespan=lifespan)
include_routers(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
