from playwright.sync_api import expect
import time
import allure
from base.base import Base
from utilities.logger import Logger

class MyNalogLogin(Base):

    url = ('http://10.250.24.48:30808/auth/login')
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


    # Locators
    login = "//input[@id='login']"
    password = "//input[@id='password']"
    registration_btn = "//button[@type='submit']"
    name_page = "//span[text()='Иванов Иван Иванович']"


    # Getters
    def get_login(self):
        return self.browser.locator(self.login)

    def get_password(self):
        return self.browser.locator(self.password)

    def get_registration_btn(self):
        return self.browser.locator(self.registration_btn)

    def get_name_page(self):
        return self.browser.locator(self.name_page)

        # Actions
    def input_login(self):
        self.get_login().fill("522401474658")

    def input_password(self):
        self.get_password().fill("1")

    def click_registration_btn(self):
        self.get_registration_btn().click()

    def my_nalog(self):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя my nalog")
            self.browser.goto(self.url)
            # self.page.url()
            self.input_login()
            self.input_password()
            self.click_registration_btn()
            expect(self.get_name_page()).to_have_text("Иванов Иван Иванович")
            time.sleep(5)
            Logger.add_end_step(method="login")

