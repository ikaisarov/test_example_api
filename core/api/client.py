import allure
import pytest
from core.api.base_client import BaseApiClient
from core.model.user import GetUserModel, NewUserModel, UpdatedUserModel
from core.model.user_list import UserListModel


class ApiClient():

    @pytest.fixture(autouse=True)
    def prepare(self, base_url, api_client):
        self.base_url: str = base_url
        self.api_client: BaseApiClient = api_client

    @allure.step("get list users")
    def get_list_users(self, page: int = 1):
        location = f'/api/users?page={page}'
        response = self.api_client._request('GET', location=location, model=UserListModel)
        return response

    @allure.step("get user")
    def get_user(self, id: int = 1):
        location = f'/api/users/{id}'
        response = self.api_client._request('GET', location=location, model=GetUserModel)
        return response

    @allure.step("create user")
    def create_user(self, user: dict):
        location = f'/api/users'
        response = self.api_client._request('POST', location=location, json_data=user, model=NewUserModel, expect_status=201)
        return response

    @allure.step("update user")
    def update_user(self, id, user: dict):
        location = f'/api/users/{id}'
        response = self.api_client._request('PUT', location=location, json_data=user, model=UpdatedUserModel)
        return response

    @allure.step("delete user")
    def delete_user(self, id):
        location = f'/api/users/{id}'
        response = self.api_client._request('DELETE', location=location, expect_status=204, jsonify=False)
        return response
