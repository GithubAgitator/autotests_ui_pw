import allure
from playwright.sync_api import sync_playwright
from pages.res_register import ResRegister


# Опции браузера

@allure.description("ResRegister")
def test_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-stage.json')
        page = context.new_page()

        res_register = ResRegister(browser, page)
        res_register.res_register()

