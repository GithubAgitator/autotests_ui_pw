from playwright.sync_api import expect

import time
import allure
from base.base import Base
from utilities.logger import Logger


class Desabled(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser


    # Locators
    registration_btn = "login-page-login-button"
    text_new = "authentication-ui-course-title-text"
    email = "//label[@id=':r0:-label']"

    # Getters
    def get_registration_btn(self):
        return self.page.get_by_test_id(self.registration_btn)

    def get_text_new(self):
        return self.page.get_by_test_id(self.text_new)

    def get_email(self):
        return self.page.locator(self.email)

        # Actions
    def click_registration_btn(self):
        expect(self.get_registration_btn()).to_be_disabled()

    def js_title(self):
        self.page.evaluate(
            """const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = 'New Text'; """
        )
        expect(self.get_text_new()).to_have_text("New Text")

    def js_email(self):
        self.page.evaluate(
            """const email = document.getElementById(':r0:-label');
            email.textContent = 'Введите ваш email'; """
        )

    def desabled(self):
        with allure.step("desabled"):
            Logger.add_start_step(method='Проверка, что кнопка неактивна')
            self.page.goto(self.url, wait_until='networkidle')
            self.page.set_viewport_size({"width": 1920, "height": 1080})
            self.click_registration_btn()
            self.js_title()
            expect(self.get_text_new()).to_have_text("New Text")
            self.js_email()
            expect(self.get_email()).to_have_text('Введите ваш email')
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Кнопка не активна, заголовок изменен")

