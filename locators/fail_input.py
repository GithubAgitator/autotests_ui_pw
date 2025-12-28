import allure
from playwright.sync_api import expect, Locator
from locators.base_elements import BaseElement

class FailInput(BaseElement):

    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file, **kwargs):
        with allure.step(f"Set file that {self.type_of} '{self.name}' set '{file}'"):
            locator = self.get_locator(**kwargs)
            locator.set_input_files(file)
