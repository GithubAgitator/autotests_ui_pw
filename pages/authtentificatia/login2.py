from playwright.sync_api import expect
from ui_coverage_tool import ActionType, SelectorType, UICoverageTracker
import time
import allure
from base.base import Base
from utilities.logger import Logger


class Login2(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser
        self.tracker = UICoverageTracker('ui-course')


    # Locators
    registration_btn = "registration-page-registration-button"
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"

    # Getters
    def get_registration_btn(self):
        return self.page.get_by_test_id(self.registration_btn)


    def get_email(self):
        return self.page.get_by_test_id(self.email).locator('input')

    def get_username(self):
        return self.page.get_by_test_id(self.username).locator('input')

    def get_password(self):
        return self.page.get_by_test_id(self.password).locator('input')

    def track_coverage(self, action_type: ActionType, locator_name: str = None):
        """Отслеживание покрытия UI"""
        if locator_name is None:
            locator_name = "unknown"

        if locator_name.startswith('//'):
            # Уже XPath — используем как есть
            selector = locator_name
        else:
            # TestID → конвертируем в XPath
            selector = f"//*[@data-testid='{locator_name}']"

        self.tracker.track_coverage(
            selector=selector,
            action_type=action_type,
            selector_type=SelectorType.XPATH
        )

        # Actions
    def desabled_registration_btn(self):
        expect(self.get_registration_btn()).to_be_disabled()
        self.track_coverage(ActionType.DISABLED, self.registration_btn)

    def input_email(self):
        self.get_email().fill('user.name@gmail.com')
        self.track_coverage(ActionType.FILL, self.email)

    def input_username(self):
        self.get_username().fill('username')
        self.track_coverage(ActionType.FILL, self.username)

    def input_password(self):
        self.get_password().fill('password')
        self.track_coverage(ActionType.FILL, self.password)

    def enabled_registration_btn(self):
        expect(self.get_registration_btn()).to_be_enabled()
        self.track_coverage(ActionType.ENABLED, self.registration_btn)


    def login2(self):
        with allure.step("login"):
            Logger.add_start_step(method='Проверка, что кнопка неактивна')
            self.page.goto(self.url, wait_until='networkidle')
            self.page.set_viewport_size({"width": 1920, "height": 1080})
            self.desabled_registration_btn()
            self.input_email()
            self.input_username()
            self.input_password()
            self.enabled_registration_btn()
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Кнопка не активна, заголовок изменен")

