import allure
import pytest
from pages.my_nalog_avtorizacia import MyNalogLogin


# Опции браузера

@allure.description("Register")
@pytest.mark.smoke
def test_reg_my_nalog(browser_page, login_password):
        login, password = login_password
        register = MyNalogLogin(browser_page)
        register.my_nalog(login, password)

