import allure
from playwright.sync_api import expect
from locators.base_elements import BaseElement

class Button(BaseElement):

    @property
    def type_of(self) -> str:
        return "button"
    def check_enable(self, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' is enable"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' is disabled"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_disabled()