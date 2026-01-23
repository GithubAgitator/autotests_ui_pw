import time
import allure
from playwright.sync_api import Page, expect
from base.base import Base
from utilities.logger import Logger
from locators.text import Text


class NavbarComponent(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    #Locators
    dashboard = "dashboard-toolbar-title-text"
    students = "students-widget-title-text"

    #Getters
    def get_dasboard(self):
        return Text(self.browser, self.dashboard, 'Dashboard')

    def get_students(self):
        return Text(self.browser, self.students, 'Students')

    #Actions
    def text_dashboard(self):
        with allure.step("Надпись Dasboard присутствует"):
            self.get_dasboard().check_have_text('Dashboard')

    def text_students(self):
        with allure.step("Надпись Students присутствует"):
            self.get_students().check_visible()
            self.get_students().check_have_text('Students')

    def navbar(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="Страница с дашбордом")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
            time.sleep(5)
            self.text_dashboard()
            self.text_students()
            Logger.add_end_step(method="Dashboard")