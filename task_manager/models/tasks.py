from .base import TunedModel


class Task(TunedModel):
    task_id: int
    title: str
    description: str
    assign_to_id: int
    created_at: str
    status: str
