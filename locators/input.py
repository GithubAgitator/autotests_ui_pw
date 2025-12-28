import allure
from playwright.sync_api import expect, Locator
from locators.base_elements import BaseElement

class Input(BaseElement):

    @property
    def type_of(self) -> str:
        return ("input")


    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('input')

    def fill(self, value, **kwargs):
        with allure.step(f"Fill {self.type_of} '{self.name}' to value '{value}'"):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

    def check_have_value(self, value, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' has a value '{value}'"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)
