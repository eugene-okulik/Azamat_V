import pytest
import requests


BASE_URL = "https://api.restful-api.dev/objects"


@pytest.fixture()
def new_gadget_id():
    body = {
        "name": "Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "519.99",
            "Capacity": "256 GB"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        BASE_URL,
        json=body,
        headers=headers
    )
    gadget_id = response.json()["id"]
    yield gadget_id
    requests.delete(f"{BASE_URL}/{gadget_id}")


@pytest.fixture(scope="session")
def method_session_indicator():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def method_test_indicator():
    print("Before test")
    yield
    print("After test")


def test_get_one_gadget(new_gadget_id, method_session_indicator, method_test_indicator):
    response = requests.get(f"{BASE_URL}/{new_gadget_id}").json()
    assert response["id"] == new_gadget_id, "The gadget id isn't returned"


@pytest.mark.medium
def test_get_all_gadgets(method_session_indicator, method_test_indicator):
    response = requests.get(f"{BASE_URL}").json()
    assert len(response) == 13, "The amount of gadgets isn't correct"


@pytest.mark.critical
@pytest.mark.parametrize("body", [
    {"name": "Apple iPad Air", "date": {"Generation": "4th", "Price": "519.99", "Capacity": "256 GB"}},
    {"name": "Apple IPhone 15", "date": {"Generation": "5th", "Price": "500", "Capacity": "512 GB"}},
    {"name": "Samsung Galaxy", "date": {"Generation": "6th", "Price": "400", "Capacity": "1024 GB"}}
])
def test_add_gadget(method_session_indicator, method_test_indicator, body):
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, "Status code isn't correct"
    assert response.json()["id"], "ID isn't exist"


def test_update_one_gadget(new_gadget_id, method_test_indicator):
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
    assert response["data"]["color"] == "silver", "The color isn't exist"


def test_update_gadget_name(new_gadget_id, method_test_indicator):
    body = {
        "name": "Apple IPhone"
    }
    headers = {"Content_Type": "application/json"}
    response = requests.patch(
        f"{BASE_URL}/{new_gadget_id}",
        json=body,
        headers=headers
    ).json()
    assert response["name"] == "Apple IPhone", "The name isn't correct"


def test_delete_gadget(new_gadget_id, method_test_indicator):
    response = requests.delete(f"{BASE_URL}/{new_gadget_id}")
    assert response.status_code == 200, "The status code isn't correct"


# Commands for running the tests
# pytest -vs task_pytest.py
# pytest -vs task_pytest.py -m critical
# pytest -vs task_pytest.py -m medium
