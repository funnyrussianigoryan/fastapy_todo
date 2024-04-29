from fastapi import APIRouter, Depends
from src.controller.todo import get_todo_controller, TodoController
from src.schemas.todo import TodoListResponse, TodoListRequest

router = APIRouter()


@router.get("/lists", response_model=list[TodoListResponse])
async def get_lists(
    todo_controller: TodoController = Depends(get_todo_controller),
) -> list[TodoListResponse]:
    result = await todo_controller.get_lists()
    return result


@router.post("/lists")
async def create_lists(
    todo_request: TodoListRequest,
    todo_controller: TodoController = Depends(get_todo_controller),
):
    result = await todo_controller.create_lists(todo_request.title)
    return result


@router.delete("/lists/{list_id}")
async def delete_list():
    return
