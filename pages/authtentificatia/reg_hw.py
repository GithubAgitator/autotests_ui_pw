import allure
from base.base import Base
from utilities.logger import Logger


class RegHw(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


        # Locators
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"
    btn = "registration-page-registration-button"

        # Getters
    def get_email(self):
        return self.page.get_by_test_id(self.email).locator('input')

    def get_username(self):
        return self.page.get_by_test_id(self.username).locator('input')

    def get_password(self):
        return self.page.get_by_test_id(self.password).locator('input')

    def get_btn(self):
        return self.page.get_by_test_id(self.btn)

    # Actions

    def input_email(self):
        self.get_email().fill('hjk@gmail.com')

    def input_username(self):
        self.get_username().fill('Daria')

    def input_password(self):
        self.get_password().fill('password')

    def click_btn(self):
        self.get_btn().click()

    def reg_hw(self):
        with allure.step("register"):
            Logger.add_start_step(method='register')
            self.page.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            self.input_email()
            self.input_username()
            self.input_password()
            self.click_btn()
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Пользователь зарегистрирован")