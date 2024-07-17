from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    chrome_driver.quit()


def test_text_field_verification(driver):
    input_data = "Test"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_string = driver.find_element(By.ID, "id_text_string")
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)
    result_text = driver.find_element(By.ID, "result-text")
    assert result_text.text == input_data, "The text doesn't match"
    print(f"Your entered text: {result_text.text}")
