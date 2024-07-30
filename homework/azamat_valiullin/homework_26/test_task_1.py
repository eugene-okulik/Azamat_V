from playwright.sync_api import Page


def test_form_authentication(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    link = page.get_by_role("link", name="Form Authentication")
    link.click()

    user_name = page.get_by_role("textbox", name="Username")
    user_name.fill("tomsmith")

    password = page.get_by_role("textbox", name="Password")
    password.fill("SuperSecretPassword!")

    login_btn = page.get_by_role("button", name="Login")
    login_btn.press("Enter")

    logout_btn = page.get_by_role("link", name="Logout")
    logout_btn.click()
