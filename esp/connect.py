from esp.abs import BaseESPManager


class ESPManager(BaseESPManager):
    def user_exists(self, *args) -> bool:
        import random

        return False
        # return random.randrange(2)

    def add_user(self, *args):
        pass
