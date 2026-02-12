from playwright.sync_api import expect
import time
import allure
from ui_coverage_tool import UICoverageTracker, ActionType, SelectorType
from base.base import Base
from utilities.logger import Logger


class Avtorizacia(Base):

    url = ('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.tracker = UICoverageTracker('ui-course')


    # Locators
    email = "login-form-email-input"
    password = "//input[@type='password']"
    btn = "login-page-login-button"
    text_alert = "//div[text()='Wrong email or password']"


    # Getters
    def get_email(self):
        return self.browser.get_by_test_id(self.email).locator('input')

    def get_password(self):
        return self.browser.locator(self.password)

    def get_btn(self):
        return self.browser.get_by_test_id(self.btn)

    def get_text_alert(self):
        return self.browser.locator(self.text_alert)

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
    def input_email(self, login):
        self.get_email().fill(login)
        self.track_coverage(ActionType.FILL, self.email)


    def input_password(self, password):
        self.get_password().fill(password)
        self.track_coverage(ActionType.FILL, self.password)

    def click_btn(self):
        self.get_btn().click()
        self.track_coverage(ActionType.CLICK, self.btn)

    def avtorizacia(self, login, password):
        with allure.step("register"):
            Logger.add_start_step(method="Регистрация пользователя")
            self.browser.goto(self.url)
            self.browser.set_viewport_size({"width": 1920, "height": 1080})
            # self.page.url()
            self.input_email(login)
            self.input_password(password)
            self.click_btn()
            expect(self.get_text_alert()).to_have_text("Wrong email or password")
            print('Авторизация не успешна, логин/пароль не верный')
            time.sleep(5)
            Logger.add_end_step(method="avtorizacia")

