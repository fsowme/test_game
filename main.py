from fastapi import Depends, FastAPI

from api import users
from database import schemas
from database.db_manager import DBManager
from database.models import Play, User

app = FastAPI()

app.include_router(users.router)
