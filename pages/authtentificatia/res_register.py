import allure
from base.base import Base
from utilities.logger import Logger


class ResRegister(Base):

    url = ("https://elk.stm-labs.ru/lk/elk/tax/payment")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser



    def res_register(self):
        with allure.step("register"):
            Logger.add_start_step(method='register')
            self.page.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Пользователь зарегистрирован")

