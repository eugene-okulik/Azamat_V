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
