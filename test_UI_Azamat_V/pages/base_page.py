import allure
from playwright.sync_api import Page, expect, BrowserContext
from test_UI_Azamat_V.pages.locators import base_locators as lc


class BasePage:
    base_url = "https://magento.softwaretestingboard.com"
    page_url = None
    pop_up_button = None

    def __init__(self, page: Page, context: BrowserContext):
        self.page = page
        self.context = context

    @allure.step("Open the webpage")
    def open_page(self):
        if self.page_url:
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this url")

    def find(self, locator):
        return self.page.locator(locator)

    @allure.step("Check that the response message matches the expected one")
    def message_verification(self, text):
        message = self.find(lc.text_message).first
        print(message.inner_text())
        expect(message).to_have_text(text)

    @allure.step("Delete the added product item from the compare products list")
    def delete_item_from_compare_list(self):
        self.page.wait_for_selector(lc.remove_item_loc)
        self.find(lc.remove_item_loc).click()
        self.pop_up_button = self.find(lc.pop_up_ok_button_loc)
        self.pop_up_button.click()

    @allure.step("Delete the item from the cart")
    def delete_item_from_cart(self):
        delete_icon = self.find(lc.delete_item_icon_loc)
        delete_icon.click()
        pop_up_button = self.find(lc.pop_up_ok_button_loc)
        pop_up_button.click()
