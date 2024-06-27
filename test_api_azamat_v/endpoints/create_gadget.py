import requests
import allure
from test_api_azamat_v.endpoints.base_endpoint import BaseEndpoint


class CreateGadget(BaseEndpoint):

    @allure.step("Create new gadget")
    def add_new_gadget(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.gadget_id = self.json['id']
        return self.response
