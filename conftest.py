

import pytest
from playwright.sync_api import sync_playwright, Playwright, Page


@pytest.fixture
def init_playwright() -> Playwright:
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()
    print("playwright has been stopped")


@pytest.fixture
def init_browser(init_playwright):
    headless = False
    chrome = init_playwright.chromium.launch(headless=headless, slow_mo=1000)
    yield chrome
    chrome.close()
    print("browser has been closed")


@pytest.fixture
def create_new_page_object(init_browser, request) -> Page:
    page = init_browser.new_page()
    request.cls.page = page
    yield page
    page.close()
    print("Page has been closed")


