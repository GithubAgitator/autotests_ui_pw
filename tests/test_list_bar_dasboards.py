import allure
from pages.list_logout import LogoutSing
from pages.courses.list_courses import CourseSing
from pages.list_dasboard import DasboardSing


# Опции браузера

@allure.description("ListMeni")
def test_list_menu(browser_pages_2):
    d = DasboardSing(browser_pages_2)
    d.list_dasboards()
    c = CourseSing(browser_pages_2)
    c.list_courses()
    l = LogoutSing(browser_pages_2)
    l.list_logout()