import time
import allure
from playwright.sync_api import expect
from base.base import Base
from utilities.logger import Logger
from components.list_meni import ListMenu


class CourseSing(Base):

    url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.components_list_menu = ListMenu(browser, 'courses')


    def list_courses(self):
        with allure.step("course"):
            Logger.add_start_step(method="Courses")
            self.browser.goto(self.url)
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            self.components_list_menu.check_courses('Courses')
            self.components_list_menu.check_icon()
            self.components_list_menu.click_button()
            self.check_current_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
            time.sleep(5)
            Logger.add_end_step(method="Courses")

