from locust import task, HttpUser
import random


class Gadgets(HttpUser):

    @task(1)
    def get_all_gadgets_performance(self):
        self.client.get(
            "/objects",
            headers={"Content-Type": "application/json"}
        )

    @task(3)
    def get_one_gadget_performance(self):
        self.client.get(
            f"/objects/{random.choice([3, 5, 10])}",
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def create_gadget_performance(self):
        self.client.post(
            "/objects",
            json={
                  "name": "Apple iPad Air",
                  "data": {
                      "Generation": "4th",
                      "Price": "519.99",
                      "Capacity": "256 GB"
                  }
            },
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def update_one_gadget_performance(self):
        self.client.put(
            "/objects/10",
            json={
                  "name": "Apple iPad Air",
                  "data": {
                      "Generation": "4th",
                      "Price": "519.99",
                      "Capacity": "256 GB",
                      "color": "silver"
                  }
            },
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def update_one_gadget_item_performance(self):
        self.client.patch(
            "/objects/10",
            json={"name": "Apple IPhone"},
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def delete_gadget_performance(self):
        self.client.delete(
            "/objects/10",
            headers={"Content-Type": "application/json"}
        )
