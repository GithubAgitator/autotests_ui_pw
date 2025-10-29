import allure
from playwright.sync_api import sync_playwright
from pages.register import Register


# Опции браузера

@allure.description("Register")
def test_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        register = Register(browser, page)
        register.register()
        context.storage_state(path='browser-stage.json')
