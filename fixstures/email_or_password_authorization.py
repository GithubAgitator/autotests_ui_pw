import pytest


"""Фикстура для логина и пароля"""
@pytest.fixture(params=[
    ("78", "password"),
    ("7", "  "),
    ("  ", "password"),
    ("12", "password")
])
def login_password(request):
    return request.param
