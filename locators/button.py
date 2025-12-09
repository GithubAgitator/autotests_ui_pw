from playwright.sync_api import expect
from locators.base_elements import BaseElement

class Button(BaseElement):
    def check_enable(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_enabled()

    def check_desabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_disabled()