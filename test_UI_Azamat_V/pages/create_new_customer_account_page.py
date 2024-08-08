import allure
from playwright.sync_api import expect
from test_UI_Azamat_V.pages.base_page import BasePage
from test_UI_Azamat_V.pages.locators import login_creation_locators as loc


class CustomerNewAccount(BasePage):

    page_url = "/customer/account/create/"

    def fill_first_name_field(self, name):
        first_name = self.page.get_by_test_id(loc.first_name_loc)
        first_name.fill(name)

    def fill_last_name_field(self, surname):
        last_name = self.page.get_by_test_id(loc.last_name_loc)
        last_name.fill(surname)

    def fill_email_field(self, email):
        email_field = self.page.get_by_test_id(loc.email_field_loc)
        email_field.fill(email)

    def fill_password_field(self, name):
        password_field = self.page.get_by_test_id(loc.password_field_loc)
        password_field.fill(name)

    def fill_password_confirmation_field(self, password_confirmation):
        password_confirm_field = self.page.get_by_test_id(loc.password_confirmation_field_loc)
        password_confirm_field.fill(password_confirmation)

    def click_create_account(self):
        create_account_button = self.find(loc.submit_button_loc)
        create_account_button.click()

    @allure.step("Fill the login form")
    def fill_login_form(self, name, surname, email, password, password_confirmation):
        self.fill_first_name_field(name)
        self.fill_last_name_field(surname)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.fill_password_confirmation_field(password_confirmation)
        self.click_create_account()

    @allure.step("Check that the reply message matches the expected one")
    def invalid_email_message_verification(self, text):
        error_message = self.page.get_by_test_id(loc.invalid_email_message_loc)
        print(error_message.inner_text())
        expect(error_message).to_have_text(text)
