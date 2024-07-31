from playwright.sync_api import Page


def test_form_filling(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name = page.get_by_role("textbox", name="First Name")
    first_name.fill("Tomas")

    last_name = page.get_by_role("textbox", name="Last Name")
    last_name.fill("Anderson")

    email_field = page.get_by_placeholder("name@example.com")
    email_field.fill("test301@mail.com")

    radio_btn = page.locator("(//*[@id='gender-radio-1'])")
    radio_btn.check(force=True)

    mobile_number = page.get_by_placeholder("Mobile Number")
    mobile_number.fill("7123456789")

    birth_date = page.locator("(//*[@id='dateOfBirthInput'])")
    birth_date.click()

    month = page.locator(".react-datepicker__month-select")
    month.select_option("January")

    year = page.locator(".react-datepicker__year-select")
    year.select_option("2000")

    day = page.locator("(//*[@aria-label='Choose Saturday, January 1st, 2000'])")
    day.click()

    subjects = page.locator("(//*[@id='subjectsInput'])")
    subjects.fill("ma")
    subjects.press("Enter")

    checkbox = page.locator("(//*[@for='hobbies-checkbox-1'])")
    checkbox.check(force=True)
    checkbox = page.locator("(//*[@for='hobbies-checkbox-3'])")
    checkbox.check(force=True)

    current_address = page.get_by_role("textbox", name="Current Address")
    current_address.fill("Test")

    state = page.locator("(//*[@id='state'])")
    state.click()
    state_option = page.locator("(//*[@id='react-select-3-option-3'])")
    state_option.click()

    city = page.locator("(//*[@id='city'])")
    city.click()
    city_option = page.locator("(//*[@id='react-select-4-option-1'])")
    city_option.click()

    submit_btn = page.locator("(//*[@id='submit'])")
    submit_btn.click()
