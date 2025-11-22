import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright


"""Фикстура для запуска теста на несколько браузеров"""
@pytest.fixture(params=['chromium', 'firefox'])
def browser_page(request: SubRequest):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        yield context.new_page()
        context.storage_state(path='browser_page_login.json')

@pytest.fixture(params=['chromium', 'firefox'])
def browser_pages_2(request: SubRequest):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False)
        context = browser.new_context(storage_state='browser-stage_reg.json')
        yield context.new_page()
