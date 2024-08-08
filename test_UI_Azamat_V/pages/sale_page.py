import allure
from playwright.sync_api import expect
from test_UI_Azamat_V.pages.base_page import BasePage
from test_UI_Azamat_V.pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    page_url = "/sale.html"
    item_details = None
    link_names_list = None
    page_titles_list = None

    @allure.step("Add item to the products compare list in another tab")
    def add_item_to_compare_list_in_another_tab(self):
        selected_items = self.find(loc.hoodies_and_sweatshirts_women_loc)
        with self.context.expect_page() as new_page_event:
            selected_items.click(modifiers=['Control'])

        new_page = new_page_event.value
        new_page.set_viewport_size({'width': 1500, 'height': 703})
        new_page.bring_to_front()
        new_page.wait_for_load_state()
        expect(new_page).to_have_title("Hoodies & Sweatshirts - Tops - Women")
        selected_item = new_page.locator(loc.item_link_loc)
        selected_item.hover()
        add_to_compare_btn = new_page.locator(loc.add_to_compare_loc)
        add_to_compare_btn.click()
        new_page.close()
        self.page.bring_to_front()
        self.page.reload()

    @allure.step("Select and add item to the shopping cart in another tab")
    def add_product_to_cart(self):
        selected_items = self.find(loc.hoodies_and_sweatshirts_men_loc)
        with self.context.expect_page() as new_page_event:
            selected_items.click(modifiers=['Control'])

        new_page = new_page_event.value
        new_page.set_viewport_size({'width': 1500, 'height': 703})
        new_page.bring_to_front()
        new_page.wait_for_load_state()
        expect(new_page).to_have_title("Hoodies & Sweatshirts - Tops - Men")
        selected_item = new_page.locator(loc.item_element_loc)
        selected_item.hover()
        item_price = new_page.get_by_test_id(loc.item_price_loc)
        item_size = new_page.locator(loc.item_size_loc)
        item_color = new_page.locator(loc.item_color_loc)
        self.item_details = {
            "name": selected_item.inner_text(),
            "price": item_price.inner_text(),
            "size": item_size.inner_text(),
            "color": item_color.get_attribute("option-label")
        }
        selected_item.hover()
        item_size.click()
        item_color.click()
        add_button = new_page.locator(loc.item_add_to_cart_loc)
        add_button.click()
        new_page.close()
        self.page.bring_to_front()
        print(self.item_details)
        self.page.reload()

    @allure.step("Open 'Mens's Deals' links in another tab")
    def click_on_links(self):
        link_list = self.find(loc.gear_link_list_loc).all()
        self.link_names_list = []
        self.page_titles_list = []
        for link in link_list:
            if link:
                link_text = link.inner_text()
                self.link_names_list.append(link_text)
                with self.context.expect_page() as new_page_event:
                    link.click(modifiers=['Control'])

                new_page = new_page_event.value
                new_page.bring_to_front()
                new_page.wait_for_load_state()
                title = new_page.title().strip()
                self.page_titles_list.append(title)
                new_page.close()
                self.page.bring_to_front()

        print(self.link_names_list)
        print(self.page_titles_list)

    @allure.step("Check the link names and the opened page titles.")
    def link_names_verification(self):
        link_names_list = self.link_names_list
        page_titles_list = self.page_titles_list
        for link in link_names_list:
            assert any(link in title for title in page_titles_list), f"Link name: {link} not found in page titles list"
