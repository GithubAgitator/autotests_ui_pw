import allure
from playwright.sync_api import sync_playwright
from pages.desabled import Desabled


# Опции браузера

@allure.description("Проверка, что кнопка неактивна")
def test_desabled():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        desabled = Desabled(browser, page)
        desabled.desabled()
