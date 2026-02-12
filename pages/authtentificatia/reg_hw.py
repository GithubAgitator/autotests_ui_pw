import allure
from base.base import Base
from utilities.logger import Logger
from ui_coverage_tool import ActionType, SelectorType, UICoverageTracker


class RegHw(Base):

    url = ("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    def __init__(self, browser, page):
        self.page = page
        super().__init__(browser)
        self.browser = browser
        self.tracker = UICoverageTracker('ui-course')


        # Locators
    email = "registration-form-email-input"
    username = "registration-form-username-input"
    password = "registration-form-password-input"
    btn = "registration-page-registration-button"

        # Getters
    def get_email(self):
        return self.page.get_by_test_id(self.email).locator('input')

    def get_username(self):
        return self.page.get_by_test_id(self.username).locator('input')

    def get_password(self):
        return self.page.get_by_test_id(self.password).locator('input')

    def get_btn(self):
        return self.page.get_by_test_id(self.btn)

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

    def input_email(self):
        self.get_email().fill('hjk@gmail.com')
        self.track_coverage(ActionType.FILL, self.email)

    def input_username(self):
        self.get_username().fill('Daria')
        self.track_coverage(ActionType.FILL, self.username)

    def input_password(self):
        self.get_password().fill('password')
        self.track_coverage(ActionType.FILL, self.password)

    def click_btn(self):
        self.get_btn().click()
        self.track_coverage(ActionType.CLICK, self.btn)

    def reg_hw(self):
        with allure.step("register"):
            Logger.add_start_step(method='register')
            self.page.goto(self.url, wait_until='networkidle')
            # self.page.set_viewport_size({"width": 1900, "height": 1040})
            self.input_email()
            self.input_username()
            self.input_password()
            self.click_btn()
            self.page.wait_for_timeout(5000)
            Logger.add_end_step(method="Пользователь зарегистрирован")