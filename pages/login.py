from playwright.sync_api import expect

import time
import allure
from base.base import Base
from utilities.logger import Logger


class Login(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"
    registration_btn = "registration-page-registration-button"
    dashbord = "//h6[@data-testid='dashboard-toolbar-title-text']"


    # Getters
    def get_email(self):
        return self.browser.get_by_test_id(self.email).locator('input')

    def get_username(self):
        return self.browser.get_by_test_id(self.username).locator('input')

    def get_password(self):
        return self.browser.get_by_test_id(self.password).locator('input')

    def get_registration_btn(self):
        return self.browser.get_by_test_id(self.registration_btn)

    def get_dashbord(self):
        return self.browser.locator(self.dashbord)

        # Actions
    def input_email(self):
        self.get_email().fill("user.name@gmail.com")

    def input_username(self):
        self.get_username().fill("username")

    def input_password(self):
        self.get_password().fill("password")

    def click_registration_btn(self):
        self.get_registration_btn().click()

    def login1(self):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email()
            self.input_username()
            self.input_password()
            self.click_registration_btn()
            expect(self.get_dashbord()).to_have_text("Dashboard")
            time.sleep(5)
            Logger.add_end_step(method="login")

