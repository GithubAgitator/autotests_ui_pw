from playwright.sync_api import expect

import time
import allure
from base.base import Base
from utilities.logger import Logger


class Avtorizacia(Base):

    url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


    # Locators
    email = "login-form-email-input"
    password = "//input[@type='password']"
    btn = "login-page-login-button"
    text_alert = "//div[text()='Wrong email or password']"


    # Getters
    def get_email(self):
        return self.browser.get_by_test_id(self.email).locator('input')

    def get_password(self):
        return self.browser.locator(self.password)

    def get_btn(self):
        return self.browser.get_by_test_id(self.btn)

    def get_text_alert(self):
        return self.browser.locator(self.text_alert)

        # Actions
    def input_email(self, login):
        self.get_email().fill(login)

    def input_password(self, password):
        self.get_password().fill(password)

    def click_btn(self):
        self.get_btn().click()

    def avtorizacia(self, login, password):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.browser.goto(self.url)
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email(login)
            self.input_password(password)
            self.click_btn()
            expect(self.get_text_alert()).to_have_text("Wrong email or password")
            print('Авторизация не успешна, логин/пароль не верный')
            time.sleep(5)
            Logger.add_end_step(method="avtorizacia")

