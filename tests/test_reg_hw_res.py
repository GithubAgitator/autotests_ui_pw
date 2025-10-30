import allure
from playwright.sync_api import sync_playwright
from pages.reg_hw_res import RegHw


# Опции браузера

@allure.description("ResRegisterHw")
def test_register():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-stage_reg.json')
        page = context.new_page()

        res_register = RegHw(browser, page)
        res_register.reg_hw()

