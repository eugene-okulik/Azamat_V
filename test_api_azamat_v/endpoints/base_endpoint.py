import allure


class BaseEndpoint:
    url = "https://api.restful-api.dev/objects"
    response = None
    json = None
    headers = {"Content_Type": "application/json"}
    gadget_id = None

    @allure.step("Make sure that the name is the same as sent in the response")
    def response_name_verification(self, name):
        assert self.json["name"] == name

    @allure.step("Make sure that response status code is 200")
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, "The status code isn't correct"

    @allure.step("Make sure that the new item is added to the response body")
    def add_new_item_verification(self, color):
        assert self.json["data"]["color"] == color, "The color isn't exist"

    @allure.step("Make sure the amount of all gadgets is 13")
    def amount_of_gadgets_verification(self):
        assert len(self.json) == 13, "The amount of gadgets isn't correct"

    @allure.step("Make sure that the new gadget id is correct")
    def gadget_id_verification(self, new_gadget_id):
        assert self.json["id"] == new_gadget_id, "The gadget id isn't correct"

    @allure.step("Make sure that the new gadget id is exist")
    def gadget_id_existing(self):
        assert self.json["id"] is not None, "The gadget id isn't returned"
