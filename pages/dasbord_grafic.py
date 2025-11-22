from playwright.sync_api import expect
import time
import allure
from base.base import Base
from utilities.logger import Logger


class Dashboard(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators
    dashboard = "//h6[@data-testid='dashboard-toolbar-title-text']"
    students = "//h6[@data-testid='students-widget-title-text']"
    students_grafic = "//div[@data-testid='students-bar-chart']"
    activities = "//h6[@data-testid='activities-widget-title-text']"
    activities_grafic = "//div[@data-testid='activities-line-chart']"
    courses = "//h6[@data-testid='courses-widget-title-text']"
    courses_grafic = "//div[@data-testid='courses-pie-chart']"
    scores = "//h6[@data-testid='scores-widget-title-text']"
    scores_grafic = "//div[@data-testid='scores-scatter-chart']"


    # Getters
    def get_dasboard(self):
        return self.browser.locator(self.dashboard)

    def get_students(self):
        return self.browser.locator(self.students)

    def get_students_grafic(self):
        return self.browser.locator(self.students_grafic)

    def get_activities(self):
        return self.browser.locator(self.activities)

    def get_activities_grafic(self):
        return self.browser.locator(self.activities_grafic)

    def get_courses(self):
        return self.browser.locator(self.courses)

    def get_courses_grafic(self):
        return self.browser.locator(self.courses_grafic)

    def get_scores(self):
        return self.browser.locator(self.scores)

    def get_scores_grafic(self):
        return self.browser.locator(self.scores_grafic)

        # Actions
    def text_dashboard(self):
        expect(self.get_dasboard()).to_have_text('Dashboard')
    def text_students(self):
        expect(self.get_students()).to_be_visible()
        expect(self.get_students()).to_have_text('Students')

    def text_students_grafic(self):
        expect(self.get_students_grafic()).to_be_visible()


    def text_activities(self):
        expect(self.get_activities()).to_be_visible()
        expect(self.get_activities()).to_have_text('Activities')

    def text_activities_grafic(self):
        expect(self.get_activities_grafic()).to_be_visible()

    def text_courses(self):
        expect(self.get_courses()).to_be_visible()
        expect(self.get_courses()).to_have_text('Courses')

    def text_courses_grafic(self):
        expect(self.get_courses_grafic()).to_be_visible()

    def text_scores(self):
        expect(self.get_scores()).to_be_visible()
        expect(self.get_scores()).to_have_text('Scores')

    def text_scores_grafic(self):
        expect(self.get_scores_grafic()).to_be_visible()

    def dashboards(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="Страница с дашбордом")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
            time.sleep(5)
            # self.browser.set_viewport_size({"width": 1920, "height": 1080})
            self.text_dashboard()
            self.text_students()
            self.text_students_grafic()
            self.text_activities()
            self.text_activities_grafic()
            self.text_scores()
            self.text_scores_grafic()
            self.text_courses()
            self.text_courses_grafic()
            Logger.add_end_step(method="Dashboard")

