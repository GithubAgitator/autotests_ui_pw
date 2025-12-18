from playwright.sync_api import expect

import time
import allure
from base.base import Base
from locators.text import Text
from utilities.logger import Logger


class AvtorizacionUser(Base):

    url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


    # Locators
    email = "login-form-email-input"
    password = "//input[@type='password']"
    btn = "login-page-login-button"
    text = "dashboard-drawer-list-item-button"


    # Getters
    def get_email(self):
        return self.browser.get_by_test_id(self.email).locator('input')

    def get_password(self):
        return self.browser.locator(self.password)

    def get_btn(self):
        return self.browser.get_by_test_id(self.btn)

    def get_text(self):
        return Text(self.browser, self.text, 'Text')

        # Actions
    def input_email(self):
        self.get_email().fill('user.name@gmail.com')

    def input_password(self):
        self.get_password().fill('password')

    def click_btn(self):
        self.get_btn().click()

    def autorizacion(self):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.browser.goto(self.url)
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email()
            self.input_password()
            self.click_btn()
            self.get_text().check_have_text('Dashboard')
            print('Dashboard')
            time.sleep(5)
            Logger.add_end_step(method="avtorizacia")

