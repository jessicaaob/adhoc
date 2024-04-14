# venv: youtube_auto
# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright

#by calling like the below it closes the browser when finished so there is nothing left open, causing memory issues

with sync_playwright() as p:
    #by default playwright runs headless, so if you want to see the browser, you need to do headless-False
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
