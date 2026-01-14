import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright
import allure
from config import settings
from tools.playwright.mocks import mock_static_resourses

"""Фикстура для запуска теста на несколько браузеров"""
@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest):
    browser_name = request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=settings.headless)
        context = browser.new_context(record_video_dir=settings.videos_dir)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page

        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        context.storage_state(path='browser_page_login.json')

        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

@pytest.fixture(params=settings.browsers)
def browser_pages_2(request: SubRequest):
    browser_name = request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=settings.headless)
        context = browser.new_context(record_video_dir=settings.videos_dir, no_viewport=True,
                                          storage_state=settings.browser_state_file,
                                      viewport=settings.viewport_settings.desktop,
                                               )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        mock_static_resourses(page)
        yield page
        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))

        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
