from pydantic import BaseModel, Extra


class BaseApiModel(BaseModel):
    class Config:
        extra = Extra.forbid
