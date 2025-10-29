from playwright.sync_api import expect

import time
import allure
from base.base import Base
from utilities.logger import Logger


class Login2(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


    # Locators
    registration_btn = "registration-page-registration-button"
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"

    # Getters
    def get_registration_btn(self):
        return self.page.get_by_test_id(self.registration_btn)


    def get_email(self):
        return self.page.get_by_test_id(self.email).locator('input')

    def get_username(self):
        return self.page.get_by_test_id(self.username).locator('input')

    def get_password(self):
        return self.page.get_by_test_id(self.password).locator('input')

        # Actions
    def desabled_registration_btn(self):
        expect(self.get_registration_btn()).to_be_disabled()

    def input_email(self):
        self.get_email().fill('user.name@gmail.com')

    def input_username(self):
        self.get_username().fill('username')

    def input_password(self):
        self.get_password().fill('password')

    def enabled_registration_btn(self):
        expect(self.get_registration_btn()).to_be_enabled()


    def login2(self):
        with allure.step("login"):
            Logger.add_start_step(method='Проверка, что кнопка неактивна')
            self.page.goto(self.url, wait_until='networkidle')
            self.page.set_viewport_size({"width": 1920, "height": 1080})
            self.desabled_registration_btn()
            self.input_email()
            self.input_username()
            self.input_password()
            self.enabled_registration_btn()
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Кнопка не активна, заголовок изменен")

