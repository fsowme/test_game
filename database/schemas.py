from typing import List

from pydantic import BaseModel, EmailStr


class UserPlayBase(BaseModel):
    user_id: int
    game_id: int


class UserPlayCreate(UserPlayBase):
    pass


class UserPlay(UserPlayBase):
    class Config:
        orm_mode = True


class UserPlayAnswer(BaseModel):
    in_esp: bool
    in_db: bool
    count_plays: int


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    plays: List[UserPlay] = []

    class Config:
        orm_mode = True


class UserEmail(UserBase):
    pass

    class Config:
        orm_mode = True
