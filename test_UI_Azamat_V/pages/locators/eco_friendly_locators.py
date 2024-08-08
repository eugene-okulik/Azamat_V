item_name_loc = "(//a[@class='product-item-link'])[2]"
add_to_compare_loc = "(//a[@class='action tocompare'])[1]"
selected_item_link_loc = "(//a[@class='product-item-link'])[1]"
added_item_link_loc = "(//a[@data-bind='attr: {href: product_url}, html: name'])"

item_price_loc = "product-price-1919"
item_size_loc = "(//*[@option-label='30'])[1]"
item_color_loc = "(//*[@option-label='Green'])[1]"
item_add_to_cart_loc = "(//button[@title='Add to Cart'])[2]"

cart_icon_link_loc = "(//a[@class='action showcart'])"
counter_link_loc = "(//*[@class='counter-number'])"
item_see_details_loc = "(//span[@class='toggle'])"
item_cart_link_loc = "(//a[@data-bind='attr: {href: product_url}, html: product_name'])"
item_cart_size_loc = "(//span[@data-bind='text: option.value'])[1]"
item_cart_color_loc = "(//span[@data-bind='text: option.value'])[2]"
item_cart_price_loc = "(//*[@class='minicart-price'])"
item_amount_loc = "(//span[@data-bind=\"text: getCartParam('summary_count')\"])"
item_deleted_message = "(//strong[@class='subtitle empty'])"

price_dropdown_loc = "(//div[@data-role='title'])[12]"
price_link_loc = (
    "(//a[@href='https://magento.softwaretestingboard.com/collections/eco-friendly.html?price=20-30'])"
)
price_range_loc = "(//div[@class='filter-options-item allow active']//span[@class='count'])[2]"
price_range_child_loc = "(//span[@class='filter-count-label'])[48]"
selected_items_loc = "(//li[@class='item product product-item'])"
