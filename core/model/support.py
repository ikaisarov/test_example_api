from pydantic import AnyUrl

from core.model.base_model import BaseApiModel


class UserSupportModel(BaseApiModel):
    url: AnyUrl
    text: str
