from playwright.sync_api import Locator, expect
import allure


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
        with allure.step(f"Getting locator with 'data-testid={locator}"):
            return self.browser.get_by_test_id(locator)

    def click(self, **kwargs):
        with allure.step(f"Clicking {self.type_of} '{self.name}' is visible"):
            locator = self.get_locator(**kwargs)
            locator.click()

    def check_visible(self, **kwargs):
        with allure.step(f"Checking {self.type_of} '{self.name}' is visible"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        with allure.step(f"Checking {self.type_of} '{self.name}' has text '{text}'"):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)