import time
import allure
from ui_coverage_tool import UICoverageTracker, SelectorType, ActionType

from base.base import Base
from utilities.logger import Logger
from locators.text import Text



class Dashboard(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.tracker = UICoverageTracker('ui-course')

    # Locators
    students_grafic = "students-bar-chart"
    activities = 'activities-widget-title-text'
    activities_grafic = 'activities-line-chart'
    courses = 'courses-widget-title-text'
    courses_grafic = 'courses-pie-chart'
    scores = 'scores-widget-title-text'
    scores_grafic = 'scores-scatter-chart'


    # Getters
    def get_students_grafic(self):
        return Text(self.browser, self.students_grafic, 'Students')

    def get_activities(self):
        return Text(self.browser, self.activities, 'Activates')

    def get_activities_grafic(self):
        return Text(self.browser, self.activities_grafic, 'Activities_grafic')

    def get_courses(self):
        return Text(self.browser, self.courses, 'Courses')

    def get_courses_grafic(self):
        return Text(self.browser, self.courses_grafic, 'courses_grafic')

    def get_scores(self):
        return Text(self.browser, self.scores, 'Scores')

    def get_scores_grafic(self):
        return Text(self.browser, self.scores_grafic, 'Scores_grafic')

    def track_coverage(self, action_type: ActionType, locator_name: str = None):
        """Отслеживание покрытия UI"""
        if locator_name is None:
            locator_name = "unknown"

        if locator_name.startswith('//'):
            # Уже XPath — используем как есть
            selector = locator_name
        else:
            # TestID → конвертируем в XPath
            selector = f"//*[@data-testid='{locator_name}']"

        self.tracker.track_coverage(
            selector=selector,
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

        # Actions
    def text_students_grafic(self):
        self.get_students_grafic().check_visible()


    def text_activities(self):
        self.get_activities().check_visible()
        self.get_activities().check_have_text('Activities')

    def text_activities_grafic(self):
        self.get_activities_grafic().check_visible()

    def text_courses(self):
        self.get_courses().check_visible()
        self.get_courses().check_have_text('Courses')

    def text_courses_grafic(self):
        self.get_courses_grafic().check_visible()

    def text_scores(self):
        self.get_scores().check_visible()
        self.get_scores().check_have_text('Scores')

    def text_scores_grafic(self):
        self.get_scores_grafic().check_visible()

    def dashboards(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="Страница с дашбордом")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
            time.sleep(5)
            # self.browser.set_viewport_size({"width": 1920, "height": 1080})
            self.text_students_grafic()
            self.text_activities()
            self.text_activities_grafic()
            self.text_scores()
            self.text_scores_grafic()
            self.text_courses()
            self.text_courses_grafic()
            Logger.add_end_step(method="Dashboard")

