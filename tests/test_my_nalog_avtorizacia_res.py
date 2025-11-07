import allure
from playwright.sync_api import sync_playwright
from pages.my_nalog_avtorizacia_res import MyNalogRes


# Опции браузера

@allure.description("MyNalog")
def test_register(chromium_page_with_state):
    res_register_my_nalog = MyNalogRes(chromium_page_with_state)
    res_register_my_nalog.my_nalog_res_avtorazacia()