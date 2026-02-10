import allure
from playwright.sync_api import expect
from locators.base_elements import BaseElement
from tools.logger import get_logger
from ui_coverage_tool import ActionType

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

        self.track_coverage(ActionType.ENABLED, **kwargs)

    def check_disabled(self, **kwargs):
        step = f"Checking that {self.type_of} '{self.name}' is disabled"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, **kwargs)
