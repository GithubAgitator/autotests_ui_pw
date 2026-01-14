import allure
from playwright.sync_api import expect, Locator
from locators.base_elements import BaseElement
from tools.logger import get_logger

logger = get_logger("FAILINPUT")
class FailInput(BaseElement):

    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file, **kwargs):
        step = f"Set file that {self.type_of} '{self.name}' set '{file}'"
        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.set_input_files(file)
