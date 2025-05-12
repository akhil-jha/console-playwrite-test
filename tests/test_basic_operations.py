def test_screenshot(login_console):
    login_console.wait_for_timeout(10_000)
    login_console.screenshot(path="loggedin.png")
