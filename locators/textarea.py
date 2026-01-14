import allure
from playwright.sync_api import expect, Locator
from locators.base_elements import BaseElement
from tools.logger import get_logger

logger = get_logger("TEXTAREA")
class TextArea(BaseElement):

    @property
    def type_of(self) -> str:
        return ("textare"
                "")
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator('textarea').first

    def fill(self, value, **kwargs):
        step = f"Fill that {self.type_of} '{self.name}' fill '{value}'"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.fill(value)

    def check_have_value(self, value, **kwargs):
        with allure.step(f"Checking that {self.type_of} '{self.name}' has a value '{value}'"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)