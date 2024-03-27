import json
import time

from playwright.sync_api import sync_playwright


class BaseSetup:
    def __init__(self):
        with open("../source/config.json") as con:
            self.data = json.load(con)
            self.username = self.data['username']
            self.password = self.data['password']


class Login(BaseSetup):
    def __init__(self):
        super().__init__()
        self.page = None

    def connect_to_website(self, username=None, password=None):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page(no_viewport=True)
            page.goto(self.data['url'])
            un = page.get_by_placeholder('Username')
            ps = page.get_by_placeholder("Password")
            # default username and password
            if username is None or password is None:
                un.fill(self.username)
                ps.fill(self.password)
            # custom username and password
            else:
                un.fill(username)
                ps.fill(password)
            # Click on connect button
            page.locator('button', has_text='Login').click()
            time.sleep(30)

    # def get_login_status(self):
    #     """ Return True if login success, False if login failed. """
    #     url = self.page
