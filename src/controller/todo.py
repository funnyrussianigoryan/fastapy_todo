import uuid

from databases import Database
from sqlalchemy import select, insert

from src.db.models import TodoList
from src.api.todo_list import TodoListResponse


class TodoController:
    def __init__(self, db: Database):
        self.db = db

    async def get_lists(self) -> list[TodoListResponse]:
        query = select(TodoList)
        rows = await self.db.fetch_all(query)
        result = [dict(row) for row in rows]
        return [
            TodoListResponse(id=row.get("id"), title=row.get("title")) for row in result
        ]

    def create_lists(self, title: str) -> TodoListResponse:
        list_id = uuid.uuid4()
        await self.db.execute(insert(TodoList).values(id=list_id, title=title))
        return TodoListResponse(id=list_id, title=title)

    def update_todo(self):
        return

    def delete_todo(self):
        return


todo_controller: TodoController = None


def get_todo_controller():
    if todo_controller is None:
        raise RuntimeError("TodoController is not initialized")
    return todo_controller
