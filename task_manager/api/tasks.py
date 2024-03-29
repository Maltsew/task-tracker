"""
api взаимодейтсвие сервиса с routers
"""
from typing import List, Union

from fastapi import Depends
from fastapi import APIRouter

from ..models.tasks import Task, ShowTask, CreateTask
from ..services.tasks import TasksService


router = APIRouter(
    prefix='/tasks',
)


@router.get('/', response_model=List[ShowTask])
async def get_tasks(service: TasksService = Depends()):
    """ Получить список всех задач"""
    return await service.get_all_tasks()


@router.post('/', response_model=ShowTask)
async def create_task(task_body: CreateTask, service: TasksService = Depends()):
    """ Создать задачу"""
    return await service.create_task(
        title=task_body.title,
        description=task_body.description,
        assign_to_id=task_body.assign_to_id,
        status=task_body.status
    )


@router.get('/{task_id}', response_model=ShowTask)
async def get_task_by_id(task_id: int, service: TasksService = Depends()):
    """ Получить задачу по id"""
    return await service.get_task_by_id(task_id)


@router.put('/{task_id}', response_model=ShowTask)
async def update_task(task_id: int, updated_task: dict, service: TasksService = Depends()):
    """ Обновление задачи по id"""
    return await service.update_task_by_id(task_id, **updated_task)


@router.get('/status/{status}', response_model=List[ShowTask])
async def get_tasks_by_status(status: str, service: TasksService = Depends()):
    """ Получить все задачи с заданным статусом"""
    return await service.get_tasks_by_status(status)


# @router.get('/created/{date}', )
