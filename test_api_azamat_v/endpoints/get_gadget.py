import requests
import allure
from test_api_azamat_v.endpoints.base_endpoint import BaseEndpoint


class GetOneGadget(BaseEndpoint):
    @allure.step("Get new gadget by id")
    def get_one_gadget(self, gadget_id):
        self.response = requests.get(f"{self.url}/{gadget_id}")
        self.json = self.response.json()
        return self.json

    @allure.step("Make sure that the new gadget id is correct")
    def gadget_id_verification(self, new_gadget_id):
        assert self.json["id"] == new_gadget_id, "The gadget id isn't correct"


class GetAllGadgets(BaseEndpoint):

    @allure.step("Get all the gadgets")
    def get_all_gadgets(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.json

    @allure.step("Make sure the amount of all gadgets is 13")
    def amount_of_gadgets_verification(self):
        assert len(self.json) == 13, "The amount of gadgets isn't correct"
