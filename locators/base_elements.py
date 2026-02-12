from playwright.sync_api import Locator, expect
import allure
from tools.logger import get_logger
from ui_coverage import tracker
from ui_coverage_tool import ActionType, SelectorType

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, browser, locator: str, name: str):
        self.browser = browser
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f"Getting locator with 'data-testid={locator}"
        with allure.step(step):
            logger.info(step)
            return self.browser.get_by_test_id(locator)

    def get_raw_locator(self, **kwargs) -> str:
        raw_locator = self.locator.format(**kwargs)
        return raw_locator if raw_locator.startswith('//') else f"//*[@data-testid='{raw_locator}']"

    def track_coverage(self, action_type: ActionType, **kwargs):
        tracker.track_coverage(
            selector=self.get_raw_locator(**kwargs),
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )



    def click(self, **kwargs):
        step = f"Clicking {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.click()

        self.track_coverage(ActionType.CLICK, **kwargs)

    def check_visible(self, **kwargs):
        step = f"Checking {self.type_of} '{self.name}' is visible"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

        self.track_coverage(ActionType.VISIBLE, **kwargs)

    def check_have_text(self, text: str, **kwargs):
        step = f"Checking {self.type_of} '{self.name}' has text '{text}'"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)

        self.track_coverage(ActionType.TEXT, **kwargs)