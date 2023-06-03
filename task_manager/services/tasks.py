"""
Сервисы выполняют бизнес-логику
"""
from typing import List, Union

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import Depends

from ..db.middleware import get_session
from ..db.tables import Task as task
from ..models.tasks import ShowTask, Task, CreateTask


class TasksService:
    """
    Управление бизнес-логикой Задач
    """
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_all_tasks(self, skip: int = 0, limit: int = 25) -> Union[List[ShowTask], None]:
        """ Возвращает список всех задач
        skip - Пропускает первых [skip] Задач
        limit - Количество отдаваемых за раз Задач"""
        tasks = (
            select(task).
            offset(skip).
            limit(limit)
        )
        query = await self.session.execute(tasks)
        result = query.scalars().all()
        if not result:
            raise HTTPException(status_code=404, detail='Tasks not found')
        return result

    async def create_task(self, title: str, description: str, assign_to_id: int, status: str) -> ShowTask:
        """ Создать новую задачу"""
        # create_task = (
        #     insert(task)
        #     .values(title=task_body.title,
        #             description=task_body.description,
        #             assign_to_id=task_body.assign_to_id,
        #             status=task_body.status)
        # )
        # await self.session.execute(create_task)
        # await self.session.commit()
        # return []
        create_task = task(title=title, description=description, assign_to_id=assign_to_id, status=status)
        self.session.add(create_task)
        await self.session.commit()
        return create_task
