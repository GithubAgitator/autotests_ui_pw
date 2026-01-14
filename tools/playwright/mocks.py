from playwright.sync_api import Page


def mock_static_resourses(page: Page):
    page.route("**/*.{ico,jpg,png}", lambda route: route.abort())
