from core.model.base_model import BaseApiModel
from core.model.user import UserModel
from core.model.support import UserSupportModel


class UserListModel(BaseApiModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserModel]
    support: UserSupportModel
