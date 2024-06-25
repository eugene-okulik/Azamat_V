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
