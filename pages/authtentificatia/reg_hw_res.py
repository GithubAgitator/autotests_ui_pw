import allure
from playwright.sync_api import expect

from base.base import Base
from utilities.logger import Logger


class RegHw(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


        # Locators
    courses = "courses-list-toolbar-title-text"
    no_results = "courses-list-empty-view-title-text"
    icon = "courses-list-empty-view-icon"
    res2 = "courses-list-empty-view-description-text"

        # Getters
    def get_courses(self):
        return self.page.get_by_test_id(self.courses)

    def get_no_results(self):
        return self.page.get_by_test_id(self.no_results)

    def get_icon(self):
        return self.page.get_by_test_id(self.icon)

    def get_res2(self):
        return self.page.get_by_test_id(self.res2)

    def reg_hw(self):
        with allure.step("register"):
            Logger.add_start_step(method='register')
            self.page.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            expect(self.get_courses()).to_have_text("Courses")
            expect(self.get_no_results()).to_have_text("There is no results")
            self.get_icon()
            self.get_res2()
            expect(self.get_res2()).to_have_text("Results from the load test pipeline will be displayed here")
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Пользователь залогинен")