from playwright.sync_api import expect
from base.base import Base


class ListMenu(Base):
    url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

    def __init__(self, browser, item):
        super().__init__(browser)
        self.item = item

        # Locators
        self.course = f'{item}-drawer-list-item-title-text'
        self.icon = f'{item}-drawer-list-item-icon'
        self.button_course = f'{item}-drawer-list-item-button'



        # Getters
    def get_course(self):
        return self.browser.get_by_test_id(self.course)

    def get_icon(self):
        return self.browser.get_by_test_id(self.icon)

    def get_button_course(self):
        return self.browser.get_by_test_id(self.button_course)

    def check_courses(self, value):
        expect(self.get_course()).to_be_visible()
        expect(self.get_course()).to_have_text(value)

    def check_icon(self):
        expect(self.get_icon()).to_be_visible()

    def click_button(self):
        expect(self.get_button_course()).to_be_visible()
        self.get_button_course().click()




