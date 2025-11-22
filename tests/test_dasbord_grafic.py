import allure
from playwright.sync_api import sync_playwright
from pages.dasbord_grafic import Dashboard


# Опции браузера

@allure.description("Dashboard")
def test_dashboard(browser_pages_2):
    dashboard = Dashboard(browser_pages_2)
    dashboard.dashboards()