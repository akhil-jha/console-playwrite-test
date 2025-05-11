import re
from playwright.sync_api import Page, expect
from .conftest import Config

def test_login_screenshot(page: Page, config: Config):
    page.goto(config.base_url)
    expect(page).to_have_title(re.compile("Log In | Red Hat IDP"))
    page.locator('input[id="username-verification"]').fill(config.username)
    page.get_by_role("button", name="Next").click()
    page.locator('input[id="password"]').fill(config.password)
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(10_000)
    page.screenshot(path="loggedin.png")
