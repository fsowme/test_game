# Test project.
## Бэкенд игры
### Причина выбора FastAPI
1. Встроенные асинхронные таски для общения с ESP
2. Возможность в будущем использовать websocket из коробки для общения с фронтом и асинхронность
### Структура
- Структура выбрана для меньшей связности частей приложения, в отдельные пакеты вынесены общие для других модули и логические части приложения.
1. Описание БД вынеесено в отдельный пакет, тк им могут пользоваться все остальные пакеты и модули.
2. Для меньшей связности API вынесено в отдельный пакет, внутри которого каждый модуль описывает работу с конкретной сущностью.
3. Функционал для работы с ESP вынесен в отдельный пакет, им могут пользоваться другие пакеты и модули.

### Запуск
- Создание виртуального окружения и клонирование репозитория:
    ```
    git clone git@github.com:fsowme/test_game.git
    cd test_game
    python -m venv venv && source venv/bin/activate
    ```
- Создание файла для хранения переменных окружения:
    ```
    touch .env && \
    echo 'DB_HOST="localhost"' > .env && \
    echo 'DB_PORT="5432"' >> .env && \
    echo 'POSTGRES_USER="postgres"' >> .env && \
    echo 'POSTGRES_PASSWORD="postgres"' >> .env && \
    echo 'POSTGRES_DB="db_name"' >> .env
    ```
- Установка зависимостей:
    ```
    pip install -r requirements.txt
    ```
- Запуск контейнера с БД
    ```
    docker-compose up -d
    ```
- Настройка БД ([миграции](https://github.com/fsowme/test_game/tree/master/migrations/versions))
    ```
    alembic upgrade <revision id последней миграции>
    uvicorn main:app
    ```
- Встроенная документация доступна по ссылке http://127.0.0.1:8000/docs

### В проекте использовались:
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) 
