from playwright.sync_api import Page, expect


def test_button_color_verification(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    red_btn = page.locator("(//*[@id='colorChange'])")
    button = "rgb(220, 53, 69)"
    expect(red_btn).to_have_css("color", button)
    red_btn.click()
