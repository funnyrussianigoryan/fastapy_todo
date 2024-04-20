from fastapi import FastAPI
from src.api import include_routers

app = FastAPI(titler="FastAPI - todo list")
include_routers(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
