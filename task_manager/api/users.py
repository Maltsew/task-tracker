from typing import List, Union

from fastapi import Depends
from fastapi import APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import select

from ..db.middleware import get_session
from ..models.users import User
from ..db.tables import User as user

router = APIRouter(
    prefix='/users',
)


@router.get('/', response_model=List[User])
async def get_users(session: Session = Depends(get_session)):
    # style 2.0
    query = select(user)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/{user_id}', response_model=User)
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)):
    query = select(user).filter(user.user_id == user_id)
    result = await session.execute(query)
    return result.scalars().first()
