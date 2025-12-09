from playwright.sync_api import expect
from base.base import Base


class CreatersImg(Base):

    def __init__(self, browser):
        super().__init__(browser)

    # Locators
    upload_image_created = "//img[@data-testid='create-course-preview-image-upload-widget-preview-image']"
    upload_image_button = 'create-course-preview-image-upload-widget-upload-button'

    def get_upload_image_button(self):
        return self.browser.get_by_test_id(self.upload_image_button).locator('input')

    def get_upload_image_created(self):
        return self.browser.locator(self.upload_image_created)

    def created_upload_image_button(self, value):
        expect(self.get_upload_image_button()).to_be_visible()
        self.get_upload_image_button().set_input_files(value)

    def visible_upload_image_created(self):
        expect(self.get_upload_image_created()).to_be_visible()
        print('Картинка загружена')

