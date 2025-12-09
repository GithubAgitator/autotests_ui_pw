from playwright.sync_api import expect, Locator
from locators.base_elements import BaseElement

class FailInput(BaseElement):
    def set_input_files(self, file, **kwargs):
        locator = self.get_locator(**kwargs)
        locator.set_input_files(file)
