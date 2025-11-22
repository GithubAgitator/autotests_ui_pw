import pytest
from playwright.sync_api import Page, Playwright, sync_playwright


@pytest.fixture
def chromium_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser.new_page()

@pytest.fixture(scope="session")
def avtorizacia_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        yield context.new_page()
        context.storage_state(path='browser-state_my_nalog.json')

@pytest.fixture()
def chromium_page_with_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state_my_nalog.json')
        yield context.new_page()