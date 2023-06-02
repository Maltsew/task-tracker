"""
Сервисы выполняют бизнес-логику
"""
from typing import List, Union

from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import Depends

from ..db.middleware import get_session
from ..db.tables import Task as task
from ..models.tasks import Task


class TasksService:
    """
    Управление бизнес-логикой Задач
    """
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    async def get_all_tasks(self, skip: int = 0, limit: int = 25) -> Union[List[Task], None]:
        """ Возвращает список всех задач
        skip - Пропускает первых [skip] Задач
        limit - Количество отдаваемых за раз Задач"""
        tasks = select(task).offset(skip).limit(limit)
        query = await self.session.execute(tasks)
        result = query.scalars().all()
        if not result:
            raise HTTPException(status_code=404, detail='Tasks not found')
        return result
