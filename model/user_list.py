from pydantic import BaseModel

from model.user import UserModel
from model.support import UserSupportModel


class UserListModel(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserModel]
    support: UserSupportModel
