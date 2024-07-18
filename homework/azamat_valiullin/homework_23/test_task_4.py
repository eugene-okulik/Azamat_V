from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    chrome_driver.quit()


def test_text_verification(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    element = driver.find_element(By.XPATH, "(//div[@id='start'])/button")
    element.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "(//div[@id='finish'])/h4")))
    element = driver.find_element(By.XPATH, "(//div[@id='finish'])/h4")
    assert element.text == "Hello World!"
