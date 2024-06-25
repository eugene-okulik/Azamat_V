import pytest
import requests
import allure


BASE_URL = "https://api.restful-api.dev/objects"


@allure.epic("API verification")
@allure.feature("Get request")
@allure.story("Gadget page")
@allure.title("Getting information about one gadget")
def test_get_one_gadget(new_gadget_id, method_session_indicator, method_test_indicator):
    with allure.step(f"Send request to the {BASE_URL}/{new_gadget_id}"):
        response = requests.get(f"{BASE_URL}/{new_gadget_id}").json()
    with allure.step(f"Check that the gadget id in the response message is {new_gadget_id}"):
        assert response["id"] == new_gadget_id, "The gadget id isn't returned"


@allure.epic("API verification")
@allure.feature("Get request")
@allure.story("Gadget page")
@allure.title("Getting information about all gadgets")
@pytest.mark.medium
def test_get_all_gadgets(method_session_indicator, method_test_indicator):
    with allure.step(f"Send request to the {BASE_URL}"):
        response = requests.get(f"{BASE_URL}").json()
    with allure.step("Check that the amount of gadgets is 13"):
        assert len(response) == 13, "The amount of gadgets isn't correct"


@allure.epic("API verification")
@allure.feature("Post request")
@allure.story("New gadget creation")
@allure.title("Creating new gadgets")
@pytest.mark.critical
@pytest.mark.parametrize("body", [
    {"name": "Apple iPad Air", "date": {"Generation": "4th", "Price": "519.99", "Capacity": "256 GB"}},
    {"name": "Apple IPhone 15", "date": {"Generation": "5th", "Price": "500", "Capacity": "512 GB"}},
    {"name": "Samsung Galaxy", "date": {"Generation": "6th", "Price": "400", "Capacity": "1024 GB"}}
])
def test_add_gadget(method_session_indicator, method_test_indicator, body):
    with allure.step(""):
        headers = {"Content_Type": "application/json"}
        response = requests.post(
            f"{BASE_URL}",
            json=body,
            headers=headers
        )
    with allure.step(""):
        assert response.status_code == 200, "Status code isn't correct"
    with allure.step(""):
        assert response.json()["id"], "ID isn't exist"


@allure.epic("API verification")
@allure.feature("Put request")
@allure.story("Edit an existing gadget")
@allure.title("Adding information about a gadget")
def test_update_one_gadget(new_gadget_id, method_test_indicator):
    with allure.step(f"Send request to the {BASE_URL}/{new_gadget_id} with required body and headers"):
        body = {
            "name": "Apple iPad Air",
            "data": {
                "Generation": "4th",
                "Price": "519.99",
                "Capacity": "255 GB",
                "color": "silver"
            }
        }
        headers = {"Content_Type": "application/json"}
        response = requests.put(
            f"{BASE_URL}/{new_gadget_id}",
            json=body,
            headers=headers
        ).json()
    with allure.step("Check that the new color: silver is added to the gadget information"):
        assert response["data"]["color"] == "silver", "The color isn't exist"


@allure.epic("API verification")
@allure.feature("Patch request")
@allure.story("Edit an existing gadget")
@allure.title("Changing the gadget name")
def test_update_gadget_name(new_gadget_id, method_test_indicator):
    with allure.step(f"Send request to the {BASE_URL}/{new_gadget_id} with required body and headers"):
        body = {
            "name": "Apple IPhone"
        }
        headers = {"Content_Type": "application/json"}
        response = requests.patch(
            f"{BASE_URL}/{new_gadget_id}",
            json=body,
            headers=headers
        ).json()
    with allure.step("Check that the gadget name is changed"):
        assert response["name"] == "Apple IPhone", "The name isn't correct"


@allure.epic("API verification")
@allure.feature("Delete request")
@allure.story("Delete an existing gadget")
@allure.title("Deleting information about a gadget")
def test_delete_gadget(new_gadget_id, method_test_indicator):
    with allure.step(f"Send request to the {BASE_URL}/{new_gadget_id}"):
        response = requests.delete(f"{BASE_URL}/{new_gadget_id}")
    with allure.step("Check that the status code of the response message is 200"):
        assert response.status_code == 200, "The status code isn't correct"
