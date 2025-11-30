import allure
from base.base import Base
from utilities.logger import Logger
from components.list_course import ListCourse


class CourseMenu(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.list_courses = ListCourse(browser, 'courses-list')


    def created_coursed2(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="course")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
            self.list_courses.check_icon()
            self.list_courses.check_results('There is no results')
            self.list_courses.check_res_total('Results from the load test pipeline will be displayed here')
            Logger.add_end_step(method="Coursed")

