from abc import ABC, abstractmethod


class BaseESPManager(ABC):
    @abstractmethod
    def user_exists(self, *args) -> bool:
        pass

    @abstractmethod
    def add_user(self, *args):
        pass
