import allure
from pages.login2 import Login2
from playwright.sync_api import sync_playwright, Request, Response
from pages.logger import log_request, log_response


# Опции браузера
@allure.description("Проверка активности кнопки Регистрация")
def test_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.on("request", log_request)  # Запрос отправлен
        page.on("response", log_response)

        login2 = Login2(browser, page)
        login2.login2()
