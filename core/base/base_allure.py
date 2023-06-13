import allure
import json
from typing import Any


class Allure:
    @staticmethod
    def attach_json(file: Any, name: str) -> None:
        allure.attach(json.dumps(file, sort_keys=False, ensure_ascii=False, indent=4, separators=(',', ': ')), name=name,
                      attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_text(file: str, name: str) -> None:
        allure.attach(file, name=name, attachment_type=allure.attachment_type.TEXT)
