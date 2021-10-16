from sqlalchemy.orm import Session

from database.database import DBSession


class ContextManagerDescriptor:
    def __get__(self, instance, owner):
        def context():
            with owner() as _instance:
                yield _instance

        return context

    def __set__(self, instance, value):
        raise AttributeError("Read-only attribute")


class DBManager:
    manager_as_context = ContextManagerDescriptor()

    def __init__(self) -> None:
        self.db_session: Session = DBSession()

    def commit(self, instance):
        try:
            self.db_session.add(instance)
            self.db_session.commit()
            self.db_session.refresh(instance)
        except Exception as error:
            self.db_session.rollback()
            raise error
        return instance

    def create(self, model, **kwargs):
        new_instance = model(**kwargs)
        saved_instance = self.commit(new_instance)
        return saved_instance

    def get(self, model, **kwargs):
        query = self.db_session.query(model)
        instance = query.filter_by(**kwargs).one_or_none()
        return instance

    def get_or_create(self, model, defaults: dict = None, **kwargs):
        query = self.db_session.query(model)
        if instance := query.filter_by(**kwargs).one_or_none():
            return instance, False
        object_fields = kwargs | (defaults or {})
        instance = self.create(model, **object_fields)
        return instance, True

    def filter_by(self, model, **kwargs):
        return self.db_session.query(model).filter_by(**kwargs)

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")
        self.db_session.close()
