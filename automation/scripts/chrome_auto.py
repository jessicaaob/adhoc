# venv: youtube_auto
# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright

#by calling like the below it closes the browser when finished so there is nothing left open, causing memory issues

with sync_playwright() as p:
    #by default playwright runs headless, so if you want to see the browser, you need to do headless-False
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.irishtimes.com/')
    #page.getByRole('button', { name: 'Sign In' }).click()
    page.locator('button:text("I Accept")').click()
    #page.locator('button:text("Don\'t Allow")').click()
    page.inner_html= ['#webpush-custom-prompt-button1']
    #page.locator('"Sign In")').click()
    #page.locator(":has-text(\"Sign In\")").click()
    page.locator('#main-nav :text-is("Sign In")').click()



   