from playwright.sync_api import expect

import time
import allure
from base.base import Base
from utilities.logger import Logger


class Avtorizacia(Base):

    url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


    # Locators
    email = "//div[@data-testid='login-form-email-input']//div//input"
    password = "//input[@type='password']"
    btn = "//button[text()='Login']"
    text_alert = "//div[text()='Wrong email or password']"


    # Getters
    def get_email(self):
        return self.page.locator(self.email)

    def get_password(self):
        return self.page.locator(self.password)

    def get_btn(self):
        return self.page.locator(self.btn)

    def get_text_alert(self):
        return self.page.locator(self.text_alert)

        # Actions
    def input_email(self):
        self.get_email().fill("user.name@gmail.com")

    def input_password(self):
        self.get_password().fill("password")

    def click_btn(self):
        self.get_btn().click()

    def avtorizacia(self):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.page.goto(self.url)
            self.page.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email()
            self.input_password()
            self.click_btn()
            expect(self.get_text_alert()).to_have_text("Wrong email or password")
            time.sleep(5)
            Logger.add_end_step(method="avtorizacia")

