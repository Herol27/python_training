import fastapi
import uvicorn
from fastapi import FastAPI, Response, Depends
from sqlalchemy.orm import Session

from db import models
from db import crud
from db.database import SessionLocal, engine
from db.schemas import TodoTask

app = FastAPI(title="To-do list API")


class DbInit:
    """
    Create the db schema, just once.
    """
    is_initizalized = False

    @classmethod
    def initialize(cls):
        if not cls.is_initizalized:
            models.Base.metadata.create_all(bind=engine)
            cls.is_initizalized = True


# Dependency
def get_db():
    DbInit.initialize()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.put("/tasks")
def insert_task(task: TodoTask, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, response: Response, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"
    else:
        return crud.remove_task(db, task_id=task_id)


@app.get("/tasks/{task_id}")
def select_task(task_id: int, response: Response, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"
    else:
        return db_task


@app.post("/tasks/{task_id}")
def update_task(task_id: int, task: TodoTask, response: Response, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id=task_id)
    if db_task is None:
        response.status_code = fastapi.status.HTTP_404_NOT_FOUND
        return "task not found"
    else:
        return crud.change_task(db, task_id, task)


if __name__ == '__main__':
    uvicorn.run("todolist_api:app", host="localhost", port=8080, reload=True)
