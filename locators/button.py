import allure
from playwright.sync_api import expect
from locators.base_elements import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")
class Button(BaseElement):

    @property
    def type_of(self) -> str:
        return "button"
    def check_enable(self, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is enable"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is disabled"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()