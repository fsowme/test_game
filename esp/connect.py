import random

from esp.abs import BaseESPManager


class ESPManager(BaseESPManager):
    def user_exists(self, email) -> bool:
        return random.choice(True, False)

    def add_user(self, email):
        pass
