import time

import allure
from playwright.sync_api import Page, expect
from base.base import Base
from utilities.logger import Logger


class NavbarComponent(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    #Locators
    dashboard = "//h6[@data-testid='dashboard-toolbar-title-text']"
    students = "//h6[@data-testid='students-widget-title-text']"

    #Getters
    def get_dasboard(self):
        return self.browser.locator(self.dashboard)

    def get_students(self):
        return self.browser.locator(self.students)

    #Actions
    def text_dashboard(self):
        expect(self.get_dasboard()).to_have_text('Dashboard')
    def text_students(self):
        expect(self.get_students()).to_be_visible()
        expect(self.get_students()).to_have_text('Students')

    def navbar(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="Страница с дашбордом")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
            time.sleep(5)
            self.text_dashboard()
            self.text_students()
            Logger.add_end_step(method="Dashboard")