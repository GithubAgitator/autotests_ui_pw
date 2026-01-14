import time
from playwright.sync_api import expect
import allure
from base.base import Base
from tools.logger import get_logger
from utilities.logger import Logger
from components.course_components import Coursed
from components.creater_img_components import CreatersImg


logger = get_logger("CREATECOURSE")

class CreateCourse(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.components_course = Coursed(browser)
        self.img = CreatersImg(browser)

    # Locators
    create_course = "//h6[@data-testid='create-course-toolbar-title-text']"
    create_button_course_desable = "//button[@data-testid='create-course-toolbar-create-course-button']"
    icon = "create-course-preview-empty-view-icon"
    image_selected = "//h6[@data-testid='create-course-preview-empty-view-title-text']"
    preview_image_selected = "//p[@data-testid='create-course-preview-empty-view-description-text']"
    upload_image = "//p[@data-testid='create-course-preview-image-upload-widget-info-title-text']"
    upload_image_button = "create-course-preview-image-upload-widget-upload-button"
    title = "//input[@id=':r0:']"
    estemated_time = "//input[@id=':r1:']"
    description = "//textarea[@id=':r2:']"
    max_score = "//input[@id=':r3:']"
    min_score = "//input[@id=':r4:']"






    # Getters
    def get_create_course(self):
        return self.browser.locator(self.create_course)

    def get_create_button_course_desable(self):
        return self.browser.locator(self.create_button_course_desable)

    def get_visible_icon(self):
        return self.browser.get_by_test_id(self.icon)

    def get_image_selected(self):
        return self.browser.locator(self.image_selected)

    def get_preview_image_selected(self):
        return self.browser.locator(self.preview_image_selected)

    def get_upload_image(self):
        return self.browser.locator(self.upload_image)

    def get_upload_image_button(self):
        return self.browser.get_by_test_id(self.upload_image_button).locator('input')

    def get_title(self):
        return self.browser.locator(self. title)

    def get_estemated_time(self):
        return self.browser.locator(self.estemated_time)

    def get_description(self):
        return self.browser.locator(self.description)

    def get_max_score(self):
        return self.browser.locator(self.max_score)

    def get_min_score(self):
        return self.browser.locator(self.min_score)

        # Actions
    def text_create_course(self):
        step = f"Кнопка создание курса"
        with allure.step(step):
            logger.info(step)
            expect(self.get_create_course()).to_have_text('Create course')

    def visible_create_button_course_desable(self):
        step = f"Кнопка для создания курсов присутствует"
        with allure.step(step):
            logger.info(step)
            expect(self.get_create_button_course_desable()).to_be_disabled()
            print('Кнопка для создания курсов присутствует')

    def visible_icon(self):
        step = "Иконка курсов видна"
        with allure.step(step):
            logger.info(step)
            expect(self.get_visible_icon()).to_be_visible()

    def visibled_image_selected(self):
        expect(self.get_image_selected()).to_be_visible()
        expect(self.get_image_selected()).to_have_text('No image selected')
        print('No image selected')

    def visibled_preview_image_selected(self):
        expect(self.get_preview_image_selected()).to_be_visible()
        expect(self.get_preview_image_selected()).to_have_text('Preview of selected image will be displayed here')
        print('Preview of selected image will be displayed here')

    def visibled_upload_image(self):
        expect(self.get_upload_image()).to_be_visible()
        expect(self.get_upload_image()).to_have_text('Tap on "Upload image" button to select file')
        print('Tap on "Upload image" button to select file')



    def input_title(self):
        step = f"Ввели название курсов"
        with allure.step(step):
            logger.info(step)
            self.get_title().fill('Test')

    def input_time(self):
        step = "Время прохождения курса"
        with allure.step(step):
            logger.info(step)
            self.get_estemated_time().fill('4h')

    def input_description(self):
        step = f"Описание курса"
        with allure.step(step):
            logger.info(step)
            self.get_description().fill('Python')

    def input_max_score(self):
        step = f"Максимальное количество правильных ответов"
        with allure.step(step):
            logger.info(step)
            self.get_max_score().click()
            self.get_max_score().fill('30')

    def input_min_score(self):
        step = f"Минимальное количество правильных ответов"
        with allure.step(step):
            logger.info(step)
            self.get_min_score().click()
            self.get_min_score().fill('5')

    def cteated_coursed_id(self):
        with allure.step("dashboard"):
            Logger.add_start_step(method="Created course")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
            self.text_create_course()
            self.visible_create_button_course_desable()
            self.visible_icon()
            self.visibled_image_selected()
            self.visibled_preview_image_selected()
            self.visibled_upload_image()
            self.img.created_upload_image_button('C:\\Users\\d.milyakova\\Desktop\\autotests_ui_pw\\pythonProject\\ke.jpg')
            self.img.visible_upload_image_created()
            self.components_course.check_img()
            # time.sleep(5)
            self.input_title()
            self.components_course.check_title('Test')
            self.input_time()
            self.input_description()
            self.components_course.check_description('Python')
            self.input_max_score()
            self.components_course.check_max_score('30')
            self.input_min_score()
            self.components_course.check_min_score('5')
            self.check_current_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
            Logger.add_end_step(method="Created coursed")

