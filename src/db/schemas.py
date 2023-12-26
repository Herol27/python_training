from pydantic import BaseModel


class TodoTask(BaseModel):
    task: str
    status: bool

    class Config:
        orm_mode = True