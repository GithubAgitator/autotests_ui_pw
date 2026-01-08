from playwright.sync_api import expect
import time
import allure
from base.base import Base
from utilities.logger import Logger

class MyNalogLogin(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    url = "http://10.250.24.48:30808/auth/login"


    # Locators
    login = "//input[@id='login']"
    password = "//input[@id='password']"
    registration_btn = "//button[@type='submit']"
    # name_page = "//span[text()='Неверный ИНН/пароль']"


    # Getters
    def get_login(self):
        return self.browser.locator(self.login)

    def get_password(self):
        return self.browser.locator(self.password)

    def get_registration_btn(self):
        return self.browser.locator(self.registration_btn)

    # def get_name_page(self):
    #     return self.browser.locator(self.name_page)

        # Actions
    def input_login(self, login):
        self.get_login().fill(login)

    def input_password(self, password):
        self.get_password().fill(password)

    def click_registration_btn(self):
        expect(self.get_registration_btn()).to_be_disabled()

    def my_nalog(self, login, password):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя my nalog")
            self.browser.goto(self.url)
            # self.page.url()
            self.input_login(login)
            self.input_password(password)
            self.click_registration_btn()
            time.sleep(5)
            Logger.add_end_step(method="login")

