from playwright.sync_api import expect
from ui_coverage_tool import UICoverageTracker, ActionType, SelectorType
import time
import allure
from base.base import Base
from utilities.logger import Logger
from locators.input import Input
from locators.button import Button


class Login(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.tracker = UICoverageTracker('ui-course')

    # Locators
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"
    registration_btn = "registration-page-registration-button"
    dashbord = "//h6[@data-testid='dashboard-toolbar-title-text']"
    logout = "logout-drawer-list-item-title-text"


    # Getters
    def get_email(self):
        return Input(self.browser, self.email, "email")

    def get_username(self):
        return Input(self.browser, self.username, "username")

    def get_password(self):
        return Input(self.browser,  self.password, "password")

    def get_registration_btn(self):
        return Button(self.browser, self.registration_btn, "register_btn")

    def get_dashbord(self):
        return self.browser.locator(self.dashbord)

    def get_logout(self):
        return Button(self.browser, self.logout, "logout")

        # Actions
    def input_email(self):
        self.get_email().fill("user.name@gmail.com")

    def input_username(self):
        self.get_username().fill("username")

    def input_password(self):
        self.get_password().check_visible()
        self.get_password().fill("password")

    def click_registration_btn(self):
        self.get_registration_btn().click()

    def click_logout(self):
        self.get_logout().click()

    def login1(self):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email()
            self.input_username()
            self.input_password()
            self.click_registration_btn()
            expect(self.get_dashbord()).to_have_text("Dashboard")
            self.click_logout()
            time.sleep(5)
            Logger.add_end_step(method="login")

