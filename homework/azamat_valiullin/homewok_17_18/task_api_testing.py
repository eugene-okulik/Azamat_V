import requests


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
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    return response.json()["id"]


def delete_new_gadget(gadget_id):
    requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")


def create_one_gadget():
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
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, "Status code isn't correct"
    assert response.json()["id"], "ID isn't exist"
    print(response.json()["id"])


def update_one_gadget():
    gadget_id = new_gadget_id()
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
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    ).json()
    assert response["data"]["color"] == "silver", "The color isn't exist"
    print(response)
    delete_new_gadget(gadget_id)


def update_gadget_name():
    gadget_id = new_gadget_id()
    body = {
        "name": "Apple IPhone"
    }
    headers = {"Content_Type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    ).json()
    assert response["name"] == "Apple IPhone", "The name isn't correct"
    print(response["name"])
    delete_new_gadget(gadget_id)


def delete_gadget():
    gadget_id = new_gadget_id()
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")
    assert response.status_code == 200, "The status code isn't correct"
    print(response.status_code)


def get_all_gadgets():
    response = requests.get("https://api.restful-api.dev/objects").json()
    assert len(response) == 13, "The amount of gadgets isn't correct"


def get_one_gadget():
    gadget_id = new_gadget_id()
    response = requests.get(f"https://api.restful-api.dev/objects/{gadget_id}").json()
    assert response["id"] == gadget_id, "The gadget id isn't returned"


create_one_gadget()
update_one_gadget()
update_gadget_name()
delete_gadget()
get_all_gadgets()
get_one_gadget()
