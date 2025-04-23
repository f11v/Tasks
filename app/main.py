from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
tasks = []

class Task(BaseModel):
    id: int
    name: str
    title: str
    completed: bool

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task added"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted"}
