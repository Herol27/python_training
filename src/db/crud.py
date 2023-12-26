from sqlalchemy.orm import Session

from . import models, schemas


def get_task(db: Session, task_id: int):
    return db.query(models.TodoList).filter(models.TodoList.id == task_id).first()


def create_task(db: Session, task: schemas.TodoTask):
    db_task = models.TodoList(task=task.task, status=task.status)
    db.add(db_task)
    db.commit()
    return task


def remove_task(db: Session, task_id: int):
    db.delete(db.query(models.TodoList).filter(models.TodoList.id == task_id).first())
    db.commit()
    return task_id


def change_task(db: Session, task_id: int, task: schemas.TodoTask):
    db_task = db.query(models.TodoList).filter(models.TodoList.id == task_id).first()
    db_task.task = task.task
    db_task.status = task.status
    db.commit()
    return task
