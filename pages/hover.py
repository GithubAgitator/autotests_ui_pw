from playwright.sync_api import sync_playwright, Request, Response


import time
import allure
from base.base import Base
from utilities.logger import Logger


class Hover(Base):

    url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


    # Locators
    registration_btn = "login-page-registration-link"


    # Getters
    def get_registration_btn(self):
        return self.page.get_by_test_id(self.registration_btn)

    def hover_registration_btn(self):
        self.get_registration_btn().hover()


    def hover(self):
        with allure.step("hover"):
            Logger.add_start_step(method="Наведение мышки на кнопку Регистрация")
            a = self.page.goto(self.url)
            self.page.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.hover_registration_btn()
            time.sleep(5)
            Logger.add_end_step(method="hover")

