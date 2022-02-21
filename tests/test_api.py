import allure
import pytest
import requests

from api.response import Response
from configuration.url import *
from model.user_list import UserListModel
from model.user import GetUserModel, NewUserModel, CreatedNewUserModel, UpdatedUserModel


@allure.title("Получение списка пользователей")
@pytest.mark.parametrize("page", [1, 2])
def test_get_list_users(base_url, page):
    response = Response(requests.get(base_url + GET_LIST_USERS + str(page)))

    #  Проверяем модель
    response.assert_status_code(200) \
        .validate_model(UserListModel)

    # Проверки
    assert response.response_json['page'] == page
    assert response.response_json['per_page'] == 6
    assert response.response_json['total'] == 12
    assert response.response_json['total_pages'] == 2


@allure.title("Получение одного пользователя")
@pytest.mark.parametrize("user", [1, 2])
def test_get_single_user(base_url, user):
    response = Response(requests.get(base_url + GET_USER + str(user)))

    #  Проверяем модель
    response.assert_status_code(200) \
        .validate_model(GetUserModel)

    # Проверки
    assert response.response_json['data']['id'] == user
    assert '@reqres' in response.response_json['data']['email']
    assert response.response_json['data']['avatar'] == f'https://reqres.in/img/faces/{user}-image.jpg'


@allure.title("Получение несуществующего пользователя")
@pytest.mark.parametrize("user", [100, 205])
def test_get_user_not_found(base_url, user):
    response = Response(requests.get(base_url + GET_USER + str(user)))

    # Проверки
    assert response.response_status_code == 404
    assert response.response_json == {}


@allure.title("Создание нового пользователя")
def test_create_user(base_url):
    user = NewUserModel(name="Marks", job="PM")

    response = Response(requests.post(base_url + GET_USER, json=user.dict()))

    #  Проверяем модель
    response.assert_status_code(201) \
        .validate_model(CreatedNewUserModel)

    # Проверки
    assert response.response_json['name'] == user.name
    assert response.response_json['job'] == user.job
    assert int(response.response_json['id']) > 0


@allure.title("Обновление пользователя")
def test_update_user(base_url):
    user = NewUserModel(name="John", job="dev")
    user_update = NewUserModel(name="John", job="dev-test")

    # Создаем пользователя
    Response(requests.post(base_url + GET_USER, json=user.dict()))

    # Обновляем пользователя
    response = Response(requests.put(base_url + GET_USER, json=user_update.dict()))

    #  Проверяем модель
    response.assert_status_code(200) \
        .validate_model(UpdatedUserModel)

    # Проверки
    assert response.response_json['name'] == user_update.name
    assert response.response_json['job'] == user_update.job
