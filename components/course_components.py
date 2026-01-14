from playwright.sync_api import expect
from base.base import Base
from tools.logger import get_logger


logger = get_logger("COURSED")
class Coursed(Base):

    def __init__(self, browser):
        super().__init__(browser)

        # Locators
        self.img = 'create-course-preview-image-upload-widget-preview-image'
        self.title = "//input[@id=':r0:']"
        self.times = "//input[@id=':r1:']"
        self.description = "//textarea[@id=':r2:']"
        self.max_score = "//input[@id=':r3:']"
        self.min_score = "//input[@id=':r4:']"


        # Getters
    def get_img(self):
        return self.browser.get_by_test_id(self.img)

    def get_title(self):
        return self.browser.locator(self.title)

    def get_times(self):
        return self.browser.locator(self.times)

    def get_description(self):
        return self.browser.locator(self.description)

    def get_max_score(self):
        return self.browser.locator(self.max_score)

    def get_min_score(self):
        return self.browser.locator(self.min_score)

    def check_img(self):
        expect(self.get_img()).to_be_visible()

    def check_title(self, value):
        expect(self.get_title()).to_be_visible()
        logger.info(value)
        expect(self.get_title()).to_have_value(value)

    def check_times(self, value):
        expect(self.get_times()).to_be_visible()
        logger.info(value)
        expect(self.get_times()).to_have_value(value)

    def check_description(self, value):
        expect(self.get_description()).to_be_visible()
        logger.info(value)
        expect(self.get_description()).to_have_value(value)

    def check_max_score(self, value):
        expect(self.get_max_score()).to_be_visible()
        logger.info(value)
        expect(self.get_max_score()).to_have_value(value)

    def check_min_score(self, value):
        expect(self.get_min_score()).to_be_visible()
        logger.info(value)
        expect(self.get_min_score()).to_have_value(value)






