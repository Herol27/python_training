import fastapi
import uvicorn
from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI(title="To-do list API")


class TodoTask(BaseModel):
    task: str
    status: bool


TASKS = []


@app.put("/tasks")
def insert_task(task: TodoTask):
    TASKS.append(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, response: Response):
    if len(TASKS) > task_id >= 0:
        response.status_code = fastapi.status.HTTP_200_OK
        return task_id
    else:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"


@app.get("/tasks/{task_id}")
def select_task(task_id: int, response: Response):
    if len(TASKS) > task_id >= 0:
        response.status_code = fastapi.status.HTTP_200_OK
        return TASKS[task_id]
    else:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"


@app.post("/tasks/{task_id}")
def update_task(task_id: int, task: TodoTask, response: Response):
    if len(TASKS) > task_id >= 0:
        response.status_code = fastapi.status.HTTP_200_OK
        TASKS[task_id] = task
        return TASKS[task_id]
    else:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"


if __name__ == '__main__':
    uvicorn.run("todolist_api:app", host="localhost", port=8080, reload=True)
