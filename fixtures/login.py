import re

import pytest

from conftest import Config
from playwright.sync_api import expect
from playwright.sync_api import Page


@pytest.fixture(scope="function")
def login_console(page: Page, config: Config):
    page.goto(config.base_url)
    expect(page).to_have_title(re.compile("Log In | Red Hat IDP"))
    page.locator("#truste-consent-buttons").click()
    page.locator('input[id="username-verification"]').fill(config.username)
    page.get_by_role("button", name="Next").click()
    page.locator('input[id="password"]').fill(config.password)
    page.get_by_role("button", name="Log in").click()

    yield page
