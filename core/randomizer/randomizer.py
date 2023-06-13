import random
from faker import Faker
from typing import Any

from core.enums.gender import Gender

fake = Faker()


class Randomizer:

    @staticmethod
    def random_number(start: int, end: int) -> int:
        return random.randint(start, end)

    @staticmethod
    def random_choice(array) -> Any:
        return random.choice(array)

    @staticmethod
    def random_bool() -> bool:
        return fake.pybool()

    @staticmethod
    def random_first_name(gender: Gender = Gender.MALE) -> str:
        return fake.first_name_male() if gender == Gender.MALE else fake.first_name_female()

    @staticmethod
    def random_last_name(gender: Gender = Gender.MALE) -> str:
        return fake.last_name_male() if gender == Gender.MALE else fake.last_name_female()

    @staticmethod
    def random_middle_name(gender: Gender = Gender.MALE) -> str:
        return fake.middle_name_male() if gender == Gender.MALE else fake.middle_name_female()

    @staticmethod
    def random_text() -> str:
        return fake.text()