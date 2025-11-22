import allure
from playwright.sync_api import sync_playwright

from pages.login import Login


# Опции браузера

@allure.description("Авторизация")
def test_login(browser_page: str):
     login = Login(browser_page)
     login.login1()
