import allure
from pages.authtentificatia.login import Login
from pages.authtentificatia.authtorizacion import AvtorizacionUser
from allure_commons.types import Severity


# Опции браузера

@allure.description("Авторизация")
@allure.severity(Severity.BLOCKER)
def test_login(browser_page: str):
     login = Login(browser_page)
     login.login1()
     login2 = AvtorizacionUser(browser_page)
     login2.autorizacion()