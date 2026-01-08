import allure
import pytest
from config import settings
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright, sync_playwright
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest):
    browser_name = request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=settings.headless)
        context = browser.new_context(record_video_dir=settings.videos_dir)
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page
        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))

        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

@pytest.fixture(scope="session")
def avtorizacia_user(request: SubRequest, playwright):
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name)


@pytest.fixture(params=settings.browsers)
def chromium_page_with_state(request: SubRequest):
    browser_name = request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=settings.headless)
        context = browser.new_context(record_video_dir=settings.videos_dir,
                                      storage_state='browser-state_my_nalog.json')
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        yield page

        context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
        allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

