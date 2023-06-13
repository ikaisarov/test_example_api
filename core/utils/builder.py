import json

from core.model.user import CreateUserModel
from core.randomizer.randomizer import Randomizer


class Builder:

    @staticmethod
    def random_new_user():
        random_booking = CreateUserModel(
            name=Randomizer.random_first_name(),
            job=Randomizer.random_text()
        )

        return json.loads(random_booking.json())
