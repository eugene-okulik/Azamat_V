import pytest
import allure
from faker import Faker

fake = Faker()


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with valid data")
@pytest.mark.critical
def test_new_user_account_valid_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form(fake.name(), fake.last_name(), fake.email(), "Wp60_ce#9!", "Wp60_ce#9!")
    create_new_account_page.message_verification(
        "Thank you for registering with Main Website Store."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an existing email address")
@pytest.mark.medium
def test_create_new_user_account_with_existing_data(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form("Skyla", "Kemmer", "Laurence95@yahoo.com", "VShbp3hR3", "VShbp3hR3")
    create_new_account_page.message_verification(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


@allure.feature("Create New Customer account page")
@allure.story("Creating a new customer account")
@allure.title("Create a new customer account with an invalid email address")
@pytest.mark.medium
def test_create_account_with_incorrect_email(create_new_account_page):
    create_new_account_page.open_page()
    create_new_account_page.fill_login_form("Kasandra", "Herzog", "Christoph1gmail.com", "SLcef4YBq", "SLcef4YBq")
    create_new_account_page.invalid_email_message_verification(
        "Please enter a valid email address (Ex: johndoe@domain.com)."
    )
