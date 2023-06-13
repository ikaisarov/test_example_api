import requests

from urllib.parse import urljoin
from pydantic import ValidationError
from core.base.base_allure import Allure


class BaseApiClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def _request(self, method, location, headers=None, params=None, data=None, json_data=None, model=None, expect_status=200, jsonify=True):
        url = urljoin(self.base_url, location)
        Allure.attach_text(url, name="Request url:")
        if json_data is not None:
            Allure.attach_json(json_data, name="Request body:")

        response = self.session.request(method, url, headers=headers, params=params, data=data, json=json_data)

        if response.status_code != expect_status:
            raise AssertionError(f'Request {url} failed with [{response.status_code}]: {response.text}')

        if model is not None:
            if isinstance(response.json(), list):
                for item in response.json():
                    self._validator_model_data(model, item)
            else:
                self._validator_model_data(model, response.json())

        if jsonify:
            Allure.attach_json(response.json(), name="Response json:")
            return response.json()

        return response

    def _validator_model_data(self, model, data):
        try:
            model.parse_obj(data)
        except ValidationError as e:
            raise AssertionError(e.json())
