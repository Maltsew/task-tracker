"""
Таблицы данных (Пользователь, Задача) с отображением на SQLAlchemy
"""
from typing import List, Literal
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, func


# базовый класс модели
class Base(DeclarativeBase):
    pass


class User(Base):
    """
    Модель пользователя
    """
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)

    tasks: Mapped[List["Task"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"Пользователю {self.first_name}, {self.last_name} поручено: {self.tasks}"


TaskStatus = Literal["pending", "inprogress", "completed"]


class Task(Base):
    """
    Модель,представляющая собой задачу для user
    """
    __tablename__ = 'tasks'

    task_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(140), nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    assign_to_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"))
    user: Mapped[User] = relationship(back_populates="tasks")
    created_at: Mapped[str] = mapped_column(DateTime, server_default=func.now())
    status: Mapped[TaskStatus]

    def __repr__(self) -> str:
        return f"Задача {self.title}, поручена {self.user} и имеет статус {self.status}"
