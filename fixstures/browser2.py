import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright
import allure
from allure_commons.types import AttachmentType


"""Фикстура для запуска теста на несколько браузеров"""
@pytest.fixture(params=['chromium', 'firefox'])
def browser_page(request: SubRequest):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context.new_page()

        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
        context.storage_state(path='browser_page_login.json')

        allure.attach(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')

@pytest.fixture(params=['chromium', 'firefox'])
def browser_pages_2(request: SubRequest):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=False, args=["--start-maximized"] if request.param == "chromium" else [])
        if request.param == "chromium":
            context = browser.new_context(no_viewport=True, storage_state='browser-stage_reg.json')
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        else:
            context = browser.new_context(viewport={'width': 1920, 'height': 1080},
                                          screen={'width': 1920, 'height': 1080},
                                          storage_state='browser-stage_reg.json')
            context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield context.new_page()
        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')

        allure.attach(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
