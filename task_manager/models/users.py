from .base import TunedModel


class User(TunedModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
