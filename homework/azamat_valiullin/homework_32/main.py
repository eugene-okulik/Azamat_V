from datetime import datetime
from time import sleep
import requests


def site_availability():
    while True:
        response = requests.get("https://www.google.com/")
        response_code = response.status_code
        request_time = datetime.now()
        print(f"Everything is ok: {response_code}, time: {request_time}")
        sleep(2)


site_availability()
