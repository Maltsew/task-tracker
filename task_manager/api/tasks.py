"""
api взаимодейтсвие сервиса с routers
"""
from typing import List, Union

from fastapi import Depends
from fastapi import APIRouter

from ..models.tasks import Task
from ..services.tasks import TasksService


router = APIRouter(
    prefix='/tasks',
)


@router.get('/', response_model=None)
async def get_tasks(service: TasksService = Depends()):
    return await service.get_all_tasks()
