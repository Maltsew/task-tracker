from .base import TunedModel
from pydantic import Field
from datetime import datetime


class Task(TunedModel):
    title: str
    description: str
    assign_to_id: int
    status: str


class CreateTask(Task):
    pass


class ShowTask(Task):
    task_id: int
    created_at: datetime = Field(default_factory=datetime.now)
    last_modify: datetime = Field(default_factory=datetime.now)
