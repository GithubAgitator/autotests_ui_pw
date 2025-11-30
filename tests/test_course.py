import allure
from pages.courses import CourseMenu



# Опции браузера

@allure.description("ListMeni")
def test_cousesed(browser_pages_2):
    courses = CourseMenu(browser_pages_2)
    courses.created_coursed2()
