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

    @allure.step("Make sure that the new gadget id is exist")
    def gadget_id_exists(self):
        assert self.json["id"] is not None, "The gadget id isn't returned"
