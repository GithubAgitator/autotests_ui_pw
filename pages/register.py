import allure
from base.base import Base
from utilities.logger import Logger


class Register(Base):

    url = ("https://elk.stm-labs.ru/lk/login")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


    # Locators
    inn = "//input[@name='login']"
    password = "//input[@name='password']"
    btn = "//span[text()='Войти']"


    # Getters
    def get_inn(self):
        return self.page.locator(self.inn)

    def get_password(self):
        return self.page.locator(self.password)

    def get_btn(self):
        return self.page.locator(self.btn)

        # Actions
    def input_inn(self):
        self.get_inn().fill('266276739227')

    def input_password(self):
        self.get_password().fill('test')

    def click_btn(self):
        self.get_btn().click()


    def register(self):
        with allure.step("register"):
            Logger.add_start_step(method='register')
            self.page.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            self.input_inn()
            self.input_password()
            self.click_btn()
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Пользователь зарегистрирован")

