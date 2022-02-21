from pydantic import BaseModel, AnyUrl

from model.support import UserSupportModel


class UserModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: AnyUrl


class GetUserModel(BaseModel):
    data: UserModel
    support: UserSupportModel


class NewUserModel(BaseModel):
    name: str
    job: str


class CreatedNewUserModel(BaseModel):
    name: str
    job: str
    id: int
    createdAt: str


class UpdatedUserModel(BaseModel):
    name: str
    job: str
    updatedAt: str
