import requests
import allure
from test_api_azamat_v.endpoints.base_endpoint import BaseEndpoint


class UpdateGadget(BaseEndpoint):

    @allure.step("Update gadget")
    def make_changes_in_gadget(self, gadget_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{gadget_id}",
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step("Make sure that the new item is added to the response body")
    def add_new_item_verification(self, color):
        assert self.json["data"]["color"] == color, "The color isn't exist"
