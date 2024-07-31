from playwright.sync_api import Page, expect, BrowserContext


def test_elements_verification(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    click_btn = page.get_by_role("link", name="Click")
    with context.expect_page() as new_page_event:
        click_btn.click()
    new_page = new_page_event.value
    result = new_page.locator("(//*[@id='result-text'])")
    expect(result).to_have_text("I am a new page in a new tab")
    new_page.close()
    expect(click_btn).to_be_enabled()
