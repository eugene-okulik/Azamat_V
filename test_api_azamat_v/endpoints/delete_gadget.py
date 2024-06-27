import requests
import allure
from test_api_azamat_v.endpoints.base_endpoint import BaseEndpoint


class DeleteGadget(BaseEndpoint):
    @allure.step("Delete new gadget")
    def delete_gadget(self, gadget_id):
        self.response = requests.delete(f"{self.url}/{gadget_id}")
        print(f"\nTest gadget id: {gadget_id} deleted")
