import pytest
from selenium import webdriver
from page_objects.login_page import Login_page
from utilities.readproperties import ReadConfig

class TestLoginFunctionality:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        if self._outcome.errors:
            test_method_name = self._pytestcurrentfunction.name
            self.driver.save_screenshot(f".\\Screenshots\\{test_method_name}.png")
        self.driver.quit()

    def test_homepage_title(self):
        self.driver.get(self.baseurl)
        actual_title = self.driver.title
        expected_title = "Ailaysa | Authentication"
        assert actual_title == expected_title, f"Title is '{actual_title}', but expected '{expected_title}'"

    def test_login(self):
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp = Login_page(self.driver)
        self.lp.set_email(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()

        actual_title = self.driver.title
        self.lp.profile_click()
        self.lp.logout_click()

        expected_title = "Ailaysa | Projects"
        assert actual_title == expected_title, f"Title is '{actual_title}', but expected '{expected_title}'"
