import requests
import allure
from test_api_azamat_v.endpoints.base_endpoint import BaseEndpoint


class GetOneGadget(BaseEndpoint):
    @allure.step("Get new gadget by id")
    def get_one_gadget(self, gadget_id):
        self.response = requests.get(f"{self.url}/{gadget_id}")
        self.json = self.response.json()
        return self.json


class GetAllGadgets(BaseEndpoint):

    @allure.step("Get all the gadgets")
    def get_all_gadgets(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.json
