import allure
from playwright.sync_api import sync_playwright
from pages.login import Login


# Опции браузера

@allure.description("Авторизация")
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = Login(browser, page)
        login.login1()
