from playwright.sync_api import Page, expect, sync_playwright
from conftest import Config
import pytest
import re


def _login(page, config):
    page.goto(config.base_url)
    expect(page).to_have_title(re.compile("Log In | Red Hat IDP"))
    page.locator("#truste-consent-buttons").click()
    page.locator('input[id="username-verification"]').fill(config.username)
    page.get_by_role("button", name="Next").click()
    page.locator('input[id="password"]').fill(config.password)
    page.get_by_role("button", name="Log in").click()
    return page

@pytest.fixture(scope="function")
def login_function(page: Page, config: Config):
    yield _login(page, config)


@pytest.fixture(scope="session")
def login_session(page: Page, config: Config):
    yield _login(page, config)
