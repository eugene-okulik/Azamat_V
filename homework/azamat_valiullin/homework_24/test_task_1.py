from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver


def test_phone_verification(driver):
    selected_phone = "Samsung galaxy s6"
    driver.get("https://www.demoblaze.com/index.html")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//a[contains(@href, 'prod.html?idp_=1') and contains (text(),'Samsung galaxy s6')])"))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "(//a[@class='btn btn-success btn-lg'])"))
    ).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//a[@id='cartur'])"))
    ).click()
    element_cart = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//tr[@class='success']//td[contains(text(), 'Samsung galaxy s6')])"))
    )
    assert element_cart.text in selected_phone
