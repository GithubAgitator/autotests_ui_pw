import allure
from playwright.sync_api import Playwright, Page
from config import settings, Browser
def initialize_playwright_page(playwright,
                               test_name: str,
                               browser_type: Browser,
                               storage_stage: str | None = None) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(record_video_dir=settings.videos_dir, storage_state=storage_stage)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'./tracing/{test_name}.zip'))
    allure.attach.file(f'./tracing/{test_name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)