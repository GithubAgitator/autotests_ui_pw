from playwright.sync_api import expect
from base.base import Base


class ListCourse(Base):

    def __init__(self, browser, item):
        super().__init__(browser)
        self.item = item

        # Locators
        self.icon = f'{item}-empty-view-icon'
        self.results = f'{item}-empty-view-title-text'
        self.res_total = f'{item}-empty-view-description-text'

        # Getters
    def get_icon(self):
        return self.browser.get_by_test_id(self.icon)

    def get_results(self):
        return self.browser.get_by_test_id(self.results)

    def get_res_total(self):
        return self.browser.get_by_test_id(self.res_total)

    def check_icon(self):
        expect(self.get_icon()).to_be_visible()

    def check_results(self, value):
        expect(self.get_results()).to_be_visible()
        expect(self.get_results()).to_have_text(value)

    def check_res_total(self, value):
        expect(self.get_res_total()).to_be_visible()
        expect(self.get_res_total()).to_have_text(value)





