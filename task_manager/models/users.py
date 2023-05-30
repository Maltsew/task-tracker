from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    hashed_password: str
