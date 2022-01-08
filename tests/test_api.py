import requests
from datetime import datetime
from pattern import PatternUser, PatternUsers
from pattern import NewUser, PatternNewUser, PatternUpdateUser
from pydantic import ValidationError


def test_users(base_url):
    request = requests.get(base_url + "/api/users?page=2")
    request_text = request.text

    try:
        users = PatternUsers.parse_raw(request_text)
    except ValidationError as e:
        print(e.json())
    else:
        assert users.page == 2
        assert len(users.data) == 6

        for user in users.data:
            assert "reqres.in" in user.email


def test_one_user(base_url):
    request = requests.get(base_url + "/api/users/2")
    request_text = request.text

    try:
        user = PatternUser.parse_raw(request_text)
    except ValidationError as e:
        print(e.json())
    else:
        assert user.data.id == 2
        assert user.support.url == "https://reqres.in/#support-heading"


def test_user_not_found(base_url):
    request = requests.get(base_url + "/api/users/23")
    assert request.status_code == 404


def test_create_user(base_url):
    user = NewUser("SERG", "PM")
    request = requests.post(base_url + "/api/users", user.getNewUser())
    request_text = request.text

    try:
        new_user = PatternNewUser.parse_raw(request_text)
    except ValidationError as e:
        print(e.json())
    else:
        diff_date = datetime.today() - datetime.strptime(new_user.createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        assert diff_date.days == 0
        assert new_user.name == user.name
        assert new_user.job == user.job
        assert request.status_code == 201


def test_update_user(base_url):
    user = NewUser("SERG", "CTO")
    request = requests.put(base_url + "/api/users/788", user.getNewUser())
    request_text = request.text

    try:
        new_user = PatternUpdateUser.parse_raw(request_text)
    except ValidationError as e:
        print(e.json())
    else:
        diff_date = datetime.today() - datetime.strptime(new_user.updatedAt, "%Y-%m-%dT%H:%M:%S.%fZ")
        assert diff_date.days == 0
        assert new_user.name == user.name
        assert new_user.job == user.job
        assert request.status_code == 200
