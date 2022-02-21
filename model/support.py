from pydantic import BaseModel, AnyUrl


class UserSupportModel(BaseModel):
    url: AnyUrl
    text: str
