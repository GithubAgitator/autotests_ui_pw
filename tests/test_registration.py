import allure
from playwright.sync_api import Page
from pages.register import Register


# Опции браузера

@allure.description("Register")
def test_register1(chromium_page: Page):
    register = Register(chromium_page)
    register.register()

