import pytest
import json
import time

from playwright.sync_api import sync_playwright, expect


class BaseSetup:
    def __init__(self):
        with open("source/config.json") as con:
            self.data = json.load(con)
            self.username = self.data['username']
            self.password = self.data['password']


@pytest.fixture(scope="class")
def login_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield Login(page)


class Login(BaseSetup):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def connect_to_website(self, username=None, password=None):
        self.page.goto(self.data['url'])
        un = self.page.get_by_placeholder('Username')
        ps = self.page.get_by_placeholder("Password")
        # default username and password
        if username is None or password is None:
            un.fill(self.username)
            ps.fill(self.password)
        # custom username and password
        else:
            un.fill(username)
            ps.fill(password)
        # Click on connect button
        self.page.locator('button', has_text='Login').click()
        time.sleep(5)

    def get_login_status(self):
        """ Return True if login success, False if login failed. """
        try:
            self.page.inner_text("text=Invalid credentials", timeout=1000)
            return False
        except:
            return True

    def get_username_and_password_from_ui(self):
        try:
            self.page.goto(self.data['url'])
            username_element = self.page.get_by_text("Username : Admin")
            password_element = self.page.get_by_text("Password : admin123")
            if username_element and password_element:
                username = username_element.inner_text()
                password = password_element.inner_text()
                return username, password
            else:
                return "Username or password elements not found"
        except Exception as e:
            return f"An error occurred: {e}"

    def get_login_fields_required_error(self):
        err = self.page.query_selector_all("text=Required")
        return len(err)

    def get_forget_password_element(self):
        self.page.goto(self.data['url'])
        element = self.page.get_by_text("Forgot your password?")
        element.click()
        url = self.page.url
        return url