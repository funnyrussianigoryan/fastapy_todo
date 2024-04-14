from .todo_list import router as todo_list_router
from .todo_item import router as todo_items_router


def include_routers(app):
    app.include_router(todo_list_router, tags=["lists"])
    app.include_router(todo_items_router, tags=["todos"])
