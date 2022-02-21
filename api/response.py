from pydantic import ValidationError


class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status_code = response.status_code

    def assert_status_code(self, status_code):
        assert self.response_status_code == status_code, f"\n Actual status code: {self.response_status_code} \n Expected status code: {status_code}"
        return self

    def validator_model_data(self, model, data):
        try:
            model.parse_obj(data)
        except ValidationError as e:
            raise AssertionError(
                f'{e.json()}, \nrequest_url = {self.response.url} \nresponse_json = {self.response_json}')

    def validate_model(self, model):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                self.validator_model_data(model, item)
        else:
            self.validator_model_data(model, self.response_json)
        return self
