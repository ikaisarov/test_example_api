import allure
import pytest
from hamcrest import assert_that, equal_to, contains_string, greater_than

from core.api.client import ApiClient
from core.base.base_date import BaseDate
from core.utils.builder import Builder


@allure.epic("Reqres.in")
@allure.feature("Methods API")
class TestMethodCalls(ApiClient):

    @allure.title("Get list users")
    @pytest.mark.parametrize("page", [1, 2])
    def test_get_list_users(self, page):
        with allure.step(f"get list users page: {page}"):
            list_users = self.get_list_users(page)

        with allure.step("asserts"):
            assert_that(list_users.get("page"), equal_to(page))
            assert_that(list_users.get("per_page"), equal_to(6))
            assert_that(list_users.get("total"), equal_to(12))
            assert_that(list_users.get("total_pages"), equal_to(2))

    @allure.title("Get user")
    @pytest.mark.parametrize("user_id", [1, 2])
    def test_get_user(self, user_id):
        with allure.step(f"get user: {user_id}"):
            user = self.get_user(user_id)

        with allure.step("asserts"):
            data = user.get("data")
            assert_that(data.get("id"), equal_to(user_id))
            assert_that(data.get("email"), contains_string("@reqres"))
            assert_that(data.get("avatar"), equal_to(f'https://reqres.in/img/faces/{user_id}-image.jpg'))

            support = user.get("support")
            assert_that(support.get("url"), equal_to(f"https://reqres.in/#support-heading"))
            assert_that(support.get("text"), equal_to(f"To keep ReqRes free, contributions towards server costs are appreciated!"))

    @allure.title("Create user")
    def test_create_new_user(self):
        user = Builder.random_new_user()
        date = BaseDate.date_now()

        with allure.step(f"create user"):
            new_user = self.create_user(user=user)

        with allure.step("asserts"):
            assert_that(new_user.get("name"), equal_to(user.get("name")))
            assert_that(new_user.get("job"), equal_to(user.get("job")))
            assert_that(int(new_user.get("id")), greater_than(0))
            assert_that(new_user.get("createdAt"), contains_string(date))

    @allure.title("Update user")
    def test_update_user(self):
        user = Builder.random_new_user()
        date = BaseDate.date_now()

        with allure.step(f"create user"):
            new_user = self.create_user(user)
            user_id = new_user.get("id")

        with allure.step(f"update user"):
            user_to_update = Builder.random_new_user()
            update_user = self.update_user(id=user_id, user=user_to_update)

        with allure.step("asserts"):
            assert_that(update_user.get("name"), equal_to(user_to_update.get("name")))
            assert_that(update_user.get("job"), equal_to(user_to_update.get("job")))
            assert_that(update_user.get("updatedAt"), contains_string(date))

    @allure.title("Delete user")
    def test_delete_user(self):
        user = Builder.random_new_user()

        with allure.step(f"create user"):
            new_user = self.create_user(user)
            user_id = new_user.get("id")

        with allure.step(f"delete user"):
            self.delete_user(id=user_id)
