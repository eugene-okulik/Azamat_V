import allure
from playwright.sync_api import expect
from test_UI_Azamat_V.pages.base_page import BasePage
from test_UI_Azamat_V.pages.locators import eco_friendly_locators as loc


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"
    items_amount = None
    selected_items_amount = None
    item_details = None
    cart_item_details = None
    pop_up_button = None

    @allure.step("Add the first product on the page item to the compare products list")
    def add_item_to_compare_list(self):
        selected_item = self.find(loc.selected_item_link_loc)
        add_to_compare_btn = self.find(loc.add_to_compare_loc)
        selected_item.hover()
        add_to_compare_btn.hover()
        add_to_compare_btn.click()

    @allure.step("Select a size, color and add the product item to the products cart")
    def add_item_to_cart(self):
        item_name = self.find(loc.item_name_loc)
        add_button = self.find(loc.item_add_to_cart_loc)
        item_price = self.page.get_by_test_id(loc.item_price_loc)
        item_size = self.find(loc.item_size_loc)
        item_color = self.find(loc.item_color_loc)
        self.item_details = {
            "name": item_name.inner_text(),
            "price": item_price.inner_text(),
            "size": item_size.inner_text(),
            "color": item_color.get_attribute("option-label")
        }
        print(self.item_details)
        item_name.hover()
        item_size.click()
        item_color.click()
        add_button.hover()
        add_button.click()

    @allure.step("Check and delete item from the  products cart")
    def check_item_details_in_cart(self):
        self.page.wait_for_selector(loc.counter_link_loc, state='visible')
        cart_icon = self.find(loc.cart_icon_link_loc)
        cart_icon.hover()
        cart_icon.click()
        item_cart_toggle = self.find(loc.item_see_details_loc)
        item_cart_toggle.click()
        item_cart_price = self.find(loc.item_cart_price_loc)
        item_cart_name = self.find(loc.item_cart_link_loc)
        item_cart_size = self.find(loc.item_cart_size_loc)
        item_cart_color = self.find(loc.item_cart_color_loc)
        item_cart_amount = self.find(loc.item_amount_loc)

        self.cart_item_details = {
            "name": item_cart_name.inner_text(),
            "price": item_cart_price.inner_text(),
            "size": item_cart_size.inner_text(),
            "color": item_cart_color.inner_text(),
            "amount": item_cart_amount.inner_text()
        }
        print(self.cart_item_details)

    @allure.step("Filter products by prise")
    def filter_items_by_price(self):
        dropdown_button = self.page.get_by_role("tab", name="Price")
        dropdown_button.click()
        parent_element = self.find(loc.price_range_loc)
        full_text = parent_element.inner_text()
        child_element = self.find(loc.price_range_child_loc)
        child_text = child_element.inner_text()
        items_amount = full_text.replace(child_text, '').strip()
        self.items_amount = int(items_amount)
        price_link = self.find(loc.price_link_loc)
        price_link.click()
        selected_items = self.find(loc.selected_items_loc).all()
        self.selected_items_amount = len(selected_items)

    @allure.step("Check if the number of products matches to the selected ones")
    def filtered_items_number_verification(self):
        items_amount = self.items_amount
        selected_items = self.selected_items_amount
        assert selected_items == items_amount, \
            f"Expected {items_amount} items, but found {selected_items}"

    @allure.step("Check that the added item matches the item in the shopping cart")
    def added_item_verification(self):
        selected_items = self.item_details
        items_in_cart = self.cart_item_details
        for key in selected_items:
            assert selected_items[key] == items_in_cart[key], f"{key} mismatch: {selected_items[key]} != {items_in_cart[key]}"

    @allure.step("Make sure that the added product item is in the compare products list")
    def compare_products_list_verification(self):
        selected_item = self.find(loc.selected_item_link_loc).inner_text()
        added_item = self.find(loc.added_item_link_loc).inner_text()
        print(f"Selected item: {type(selected_item)}: {selected_item}")
        print(f"Added item: {type(added_item)}: {added_item}")
        assert selected_item == added_item, f"Expected '{added_item}', but got '{selected_item}'"

    @allure.step("Check that the response message matches the expected one")
    def no_items_message_verification(self, text):
        error_message = self.find(loc.item_deleted_message)
        print(error_message.inner_text())
        expect(error_message).to_have_text(text)
