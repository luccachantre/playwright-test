from playwright.sync_api import sync_playwright, Playwright


# IMPORTANT INFO
# by default, playwright runs the script as "headless", meaning it doesnt show us the browser opening and doing all the commands
# so we can set headless = false, so that it does show the tab being opened when we run
# we can also set a property called slow_mo to change the speed of the commands so that it doesnt all happen insanely fast, 

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit"
    browser = chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://open.spotify.com")
    page.get_by_test_id("login-button").click()
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


