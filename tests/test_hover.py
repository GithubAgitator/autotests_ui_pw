import allure
from pages.hover import Hover
from playwright.sync_api import sync_playwright, Request, Response
from pages.logger import log_request, log_response


# Опции браузера
@allure.description("Проверка, что кнопка неактивна")
def test_hover():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.on("request", log_request)  # Запрос отправлен
        page.on("response", log_response)

        hover = Hover(browser, page)
        hover.hover()
