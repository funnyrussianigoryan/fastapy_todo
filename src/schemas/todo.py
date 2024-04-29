from pydantic import BaseModel


class TodoListResponse(BaseModel):
    id: str
    title: str




 class TodoListRequest(BaseModel):
     pass