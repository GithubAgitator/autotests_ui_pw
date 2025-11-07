import allure
from playwright.sync_api import expect

from base.base import Base
from utilities.logger import Logger


class MyNalogRes(Base):

    url = ("http://10.250.24.48:30808/")
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser


        # Locators
    user_name = "//span[text()='Иванов Иван Иванович']"


        # Getters
    def get_user_name(self):
        return self.browser.locator(self.user_name)


    def my_nalog_res_avtorazacia(self):
        with allure.step("avtorizacia"):
            Logger.add_start_step(method='register')
            self.browser.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            expect(self.get_user_name()).to_have_text("Иванов Иван Иванович")
            Logger.add_end_step(method="Пользователь залогинен")