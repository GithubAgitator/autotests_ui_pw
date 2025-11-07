import allure
import pytest
from pages.my_nalog_avtorizacia import MyNalogLogin


# Опции браузера

@allure.description("Register")
@pytest.mark.smoke
def test_reg_my_nalog(avtorizacia_user):
        register = MyNalogLogin(avtorizacia_user)
        register.my_nalog()

