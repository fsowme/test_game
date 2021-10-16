import random
from time import sleep

from esp.abs import BaseESPManager


class ESPManager(BaseESPManager):
    def user_exists(self, email) -> bool:
        return random.choice([False])

    def add_user(self, email):
        pass
