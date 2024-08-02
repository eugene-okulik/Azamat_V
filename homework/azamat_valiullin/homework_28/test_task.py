import re
import json
from playwright.sync_api import Page, expect, Route


def test_header_replacement(page: Page):

    header = "яблокофон 15 про"

    def handle_route(route: Route):
        server_response = route.fetch()
        body = server_response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = header
        body = json.dumps(body)
        route.fulfill(
            response=server_response,
            body=body
        )

    page.route(re.compile('library/step0_iphone/digitalmat'), handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    btn_iphone = page.get_by_role("heading", name="iPhone 15 Pro & iPhone 15 Pro")
    btn_iphone.click()
    new_header = page.get_by_role("heading", name=header)
    expect(new_header).to_have_text(header)
