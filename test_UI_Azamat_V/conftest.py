import pytest
from playwright.sync_api import BrowserContext
from test_UI_Azamat_V.pages.create_new_customer_account_page import CustomerNewAccount
from test_UI_Azamat_V.pages.login_page import LoginPage
from test_UI_Azamat_V.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_Azamat_V.pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1500, 'height': 703})
    return page


@pytest.fixture()
def create_new_account_page(page, context):
    return CustomerNewAccount(page, context)


@pytest.fixture()
def eco_friendly_page(page, context):
    return EcoFriendlyPage(page, context)


@pytest.fixture()
def sale_page(page, context):
    return SalePage(page, context)


@pytest.fixture()
def login_page(page, context):
    return LoginPage(page, context)


@pytest.fixture()
def logged_in_user(page, context):
    account = LoginPage(page, context)
    account.open_page()
    account.log_in("Laurence95@yahoo.com", "VShbp3hR3zjTdAy")
