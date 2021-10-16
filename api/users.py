from fastapi import APIRouter, BackgroundTasks, Depends

from database import schemas
from database.db_manager import DBManager
from database.models import Play, User
from esp.connect import ESPManager

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.UserPlayAnswer)
def create_user_play(
    user: schemas.UserCreate,
    background_tasks: BackgroundTasks,
    db_manager: DBManager = Depends(DBManager.manager_as_context),
    esp_manager: ESPManager = Depends(ESPManager),
):
    saved_user, is_created = db_manager.get_or_create(User, email=user.email)
    db_manager.create(Play, user_id=saved_user.id)
    in_db = not is_created
    in_esp = esp_manager.user_exists(user.email)
    if not in_esp:
        background_tasks.add_task(esp_manager.add_user, user.email)
    count_plays = db_manager.filter_by(Play, user_id=saved_user.id).count()
    data = {"in_esp": in_esp, "in_db": in_db, "count_plays": count_plays}
    answer = schemas.UserPlayAnswer(**data)
    return answer
