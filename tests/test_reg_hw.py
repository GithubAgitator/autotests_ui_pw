import allure
import pytest
from playwright.sync_api import sync_playwright
from pages.reg_hw import RegHw


# Опции браузера

@allure.description("Register")
@pytest.mark.smoke
def test_reg_hw():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        register = RegHw(browser, page)
        register.reg_hw()
        context.storage_state(path='browser-stage_reg.json')
