from datetime import datetime
from pydantic import AnyUrl

from core.model.base_model import BaseApiModel
from core.model.support import UserSupportModel


class UserModel(BaseApiModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: AnyUrl


class CreateUserModel(BaseApiModel):
    name: str
    job: str


class GetUserModel(BaseApiModel):
    data: UserModel
    support: UserSupportModel


class NewUserModel(BaseApiModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class UpdatedUserModel(BaseApiModel):
    name: str
    job: str
    updatedAt: datetime
