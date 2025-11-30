import time
import allure
from playwright.sync_api import expect
from base.base import Base
from components.list_meni import ListMenu
from utilities.logger import Logger


class LogoutSing(Base):

    url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.components_list_menu = ListMenu(browser, 'logout')


    def list_logout(self):
        with allure.step("logout"):
            Logger.add_start_step(method="Logout")
            self.browser.goto(self.url)
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            self.components_list_menu.check_courses('Logout')
            self.components_list_menu.check_icon()
            self.components_list_menu.click_button()
            self.check_current_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
            time.sleep(5)
            Logger.add_end_step(method="Logout")

