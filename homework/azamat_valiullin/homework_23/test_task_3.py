from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    chrome_driver.quit()


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    element = driver.find_element(By.XPATH, "(//select[@name='choose_language'])")
    result = driver.find_element(By.XPATH, "(//select[@name='choose_language'])/option[@value='1']")
    result_text = result.text
    selector = Select(element)
    selector.select_by_value("1")
    element = driver.find_element(By.ID, "submit-id-submit")
    element.click()
    element = driver.find_element(By.ID, "result-text")
    assert element.text == result_text
