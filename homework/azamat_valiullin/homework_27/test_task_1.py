from playwright.sync_api import Page, expect, Dialog


def test_alert(page: Page):

    def click_and_accept(alert: Dialog):
        alert.accept('Select Ok or Cancel')
        print(alert.message)
        print(alert.type)

    page.on('dialog', click_and_accept)
    # page.on('dialog', lambda alert: alert.accept('Select Ok or Cancel'))
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    click_btn = page.get_by_role('link', name='Click')
    click_btn.click()
    result_field = page.locator("(//*[@id='result-text'])")
    expect(result_field).to_have_text("Ok")
