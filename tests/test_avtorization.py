import allure
import pytest
from pages.avtorization import Avtorizacia


# Опции браузера

@allure.description("Авторизация")
def test_autorizacia(chromium_page, login_password):
    login, password = login_password
    avtorization = Avtorizacia(chromium_page)
    avtorization.avtorizacia(login, password)

