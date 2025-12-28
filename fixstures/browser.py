import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright, sync_playwright


@pytest.fixture
def chromium_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser.new_page()

@pytest.fixture(scope="session")
def avtorizacia_user(request: SubRequest):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context.new_page()
        context.storage_state(path='browser-state_my_nalog.json')
        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')

        allure.attach(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

@pytest.fixture()
def chromium_page_with_state(request: SubRequest):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state_my_nalog.json')
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context.new_page()

        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
        allure.attach(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

