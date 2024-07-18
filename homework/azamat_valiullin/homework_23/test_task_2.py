from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pytest


fake = Faker()


@pytest.fixture(scope="function")
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    yield chrome_driver
    chrome_driver.quit()


def get_by_type(locator_type):
    locator_type = locator_type.lower()
    if locator_type == "id":
        return By.ID
    elif locator_type == "name":
        return By.NAME
    elif locator_type == "xpath":
        return By.XPATH
    elif locator_type == "css":
        return By.CSS_SELECTOR
    elif locator_type == "class":
        return By.CLASS_NAME
    elif locator_type == "link":
        return By.LINK_TEXT
    elif locator_type == "tag_name":
        return By.TAG_NAME
    else:
        print("Locator type not supported")
    return False


def get_element(driver, locator, locator_type):
    element = None
    try:
        locator_type = locator_type.lower()
        by_type = get_by_type(locator_type)
        element = driver.find_element(by_type, locator)
    except Exception as e:
        print(f"Exception get element: {e}")
    return element


def send_keys(driver, data, locator="", locatorType="", element=None):
    try:
        if locator:
            element = get_element(driver, locator, locatorType)
        element.send_keys(data)
    except Exception as e:
        print(f"Exception send keys: {e}")


def element_click(driver, locator="", locatorType="", element=None):
    try:
        if locator:
            element = get_element(driver, locator, locatorType)
        element.click()
    except Exception as e:
        print(f"Exception click on element: {e} ")
        return False


def test_form_filling_verification(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    driver.execute_script("window.scrollBy(0, 700);")
    send_keys(driver, fake.name(), "firstName", "id")
    send_keys(driver, fake.last_name(), "lastName", "id")
    send_keys(driver, fake.email(), "(//input[contains(@id, 'userEmail')])", "xpath")
    element_click(driver, "//label[@for='gender-radio-1']", "xpath")
    send_keys(driver, "7982555777", "(//input[contains(@id, 'userNumber')])", "xpath")

    element_click(driver, "dateOfBirthInput", "id")
    element = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    selector = Select(element)
    selector.select_by_value("1990")
    element = driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    selector = Select(element)
    selector.select_by_value("5")
    element_click(driver, "(//div[@aria-label='Choose Sunday, June 10th, 1990'])", "xpath")

    driver.execute_script("window.scrollBy(0, 300);")
    element_click(driver, "(//label[@for='hobbies-checkbox-1'])", "xpath")

    send_keys(driver, "ma", "subjectsInput", "id")
    send_keys(driver, Keys.ENTER, "subjectsInput", "id")
    send_keys(driver, "ph", "subjectsInput", "id")
    send_keys(driver, Keys.ENTER, "subjectsInput", "id")

    send_keys(driver, fake.address(), "(//textarea[contains(@id, 'currentAddress')])", "xpath")

    element_click(driver, "(//div[@class='col-md-4 col-sm-12'])[1]", "xpath")
    element_click(driver, "(//div[@id='react-select-3-option-0'])", "xpath")

    element_click(driver, "(//div[@class='col-md-4 col-sm-12'])[2]", "xpath")
    element_click(driver, "(//div[@id='react-select-4-option-0'])", "xpath")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//button[@id='submit'])")))

    element_click(driver, "(//button[@id='submit'])", "xpath")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "(//table[@class='table table-dark table-striped table-bordered table-hover'])"))
    )
    table_element = driver.find_element(
        By.XPATH, "(//table[@class='table table-dark table-striped table-bordered table-hover'])"
    )
    table_rows = table_element.find_elements(By.TAG_NAME, "tr")
    for row in table_rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            print(cell.text)
