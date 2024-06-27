import pytest
import allure


TEST_DATA = [
    {"name": "Apple iPad Air", "date": {"Generation": "4th", "Price": "519.99", "Capacity": "256 GB"}},
    {"name": "Apple IPhone 15", "date": {"Generation": "5th", "Price": "500", "Capacity": "512 GB"}},
    {"name": "Samsung Galaxy", "date": {"Generation": "6th", "Price": "400", "Capacity": "1024 GB"}}
]

NEGATIVE_DATA = [
    {"name": "Apple iPad Air", "date": {"Generation": "4th", "Price": "519.99", "Capacity": "256 GB"}},
    {"name": "Apple IPhone 15", "date": {"Generation": "5th", "Price": "500", "Capacity": "512 GB"}},
    {"name": "Samsung Galaxy", "date": {"Generation": "6th", "Price": "400", "Capacity": "1024 GB"}}
]

TEST_DATA_PUT = {
    "name": "Apple iPad Air",
    "data": {"Generation": "4th", "Price": "519.99", "Capacity": "255 GB", "color": "silver"}
}

TEST_DATA_PATCH = {"name": "Apple IPhone"}


@allure.epic("API CRUD verification")
@allure.feature("Get request")
@allure.story("Gadget page")
@allure.title("Getting information about one gadget")
def test_get_one_gadget_by_id(get_one_gadget_endpoint, new_gadget_id_endpoint):
    get_one_gadget_endpoint.get_one_gadget(new_gadget_id_endpoint)
    get_one_gadget_endpoint.check_that_status_is_200()
    get_one_gadget_endpoint.gadget_id_verification(new_gadget_id_endpoint)


@allure.epic("API CRUD verification")
@allure.feature("Get request")
@allure.story("Gadget page")
@allure.title("Getting information about all gadgets")
def test_get_all_gadgets(get_all_gadgets_endpoint):
    get_all_gadgets_endpoint.get_all_gadgets()
    get_all_gadgets_endpoint.check_that_status_is_200()
    get_all_gadgets_endpoint.amount_of_gadgets_verification()


@allure.epic("API CRUD verification")
@allure.feature("Post request")
@allure.story("New gadget creation")
@allure.title("Creating new gadgets with valid data")
@pytest.mark.parametrize("data", TEST_DATA)
def test_add_gadget(create_gadget_endpoint, data):
    create_gadget_endpoint.add_new_gadget(payload=data)
    create_gadget_endpoint.response_name_verification(data["name"])
    create_gadget_endpoint.check_that_status_is_200()


@allure.epic("API CRUD verification")
@allure.feature("Post request")
@allure.story("New gadget creation")
@allure.title("Creating new gadgets with invalid data")
@pytest.mark.parametrize("data", NEGATIVE_DATA)
def test_add_gadget_with_negative_data(create_gadget_endpoint, data):
    create_gadget_endpoint.add_new_gadget(payload=data)
    create_gadget_endpoint.response_name_verification(data["name"])
    create_gadget_endpoint.check_that_status_is_200()
    create_gadget_endpoint.gadget_id_existing()


@allure.epic("API CRUD verification")
@allure.feature("Put request")
@allure.story("Edit an existing gadget")
@allure.title("Adding information about a gadget")
def test_update_one_gadget(update_gadget_endpoint, new_gadget_id_endpoint):
    update_gadget_endpoint.make_changes_in_gadget(new_gadget_id_endpoint, TEST_DATA_PUT)
    update_gadget_endpoint.add_new_item_verification(TEST_DATA_PUT["data"]["color"])
    update_gadget_endpoint.check_that_status_is_200()


@allure.epic("API CRUD verification")
@allure.feature("Patch request")
@allure.story("Edit an existing gadget")
@allure.title("Changing the gadget name")
def test_update_gadget_name(update_gadget_item_endpoint, new_gadget_id_endpoint):
    update_gadget_item_endpoint.update_gadget_name(new_gadget_id_endpoint, TEST_DATA_PATCH)
    update_gadget_item_endpoint.response_name_verification(TEST_DATA_PATCH["name"])
    update_gadget_item_endpoint.check_that_status_is_200()


@allure.epic("API CRUD verification")
@allure.feature("Delete request")
@allure.story("Delete an existing gadget")
@allure.title("Deleting information about a gadget")
def test_delete_gadget(delete_gadget_endpoint, delete_gadget_id_endpoint):
    delete_gadget_endpoint.delete_gadget(delete_gadget_id_endpoint)
    delete_gadget_endpoint.check_that_status_is_200()
