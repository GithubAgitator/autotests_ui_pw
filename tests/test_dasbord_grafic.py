import allure
from components.navbar_components import NavbarComponent
from pages.dasbord_grafic import Dashboard


# Опции браузера

@allure.description("Dashboard")
def test_dashboard(browser_pages_2):
    navbar = NavbarComponent(browser_pages_2)
    navbar.navbar()
    # dashboard = Dashboard(browser_pages_2)
    # dashboard.dashboards()