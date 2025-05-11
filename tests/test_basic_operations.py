import pytest
from fixtures.login import login_session, login_function

def test_login(login_function):
    login_function.wait_for_timeout(10_000)
    login_function.screenshot(path="loggedin.png")