import allure
from pages.courses.create_course import CreateCourse


# Опции браузера

@allure.description("Dashboard")
def test_created_course(browser_pages_2):
    created = CreateCourse(browser_pages_2)
    created.cteated_coursed_id()