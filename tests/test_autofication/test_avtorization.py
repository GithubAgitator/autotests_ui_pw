import allure
from pages.authtentificatia.avtorization import Avtorizacia
from tools.allure.tags import AllureTags
from allure_commons.types import Severity


# Опции браузера

@allure.title("Авторизация, выбор логина и пароля")
@allure.description("Авторизация")
@allure.tag(AllureTags.AUTHRIZATION)
@allure.severity(Severity.CRITICAL)
def test_autorizacia(chromium_page, login_password):
    # allure.dynamic.title(f'Авторизация, выбор логина и пароля {login_password}')
    login, password = login_password
    avtorization = Avtorizacia(chromium_page)
    avtorization.avtorizacia(login, password)

