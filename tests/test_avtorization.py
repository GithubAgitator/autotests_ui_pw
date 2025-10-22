import allure
from playwright.sync_api import sync_playwright
from pages.avtorization import Avtorizacia


# Опции браузера

@allure.description("Добавление спец КБК")
def test_add_spec_kbk():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        avtorization = Avtorizacia(browser, page)
        avtorization.avtorizacia()
