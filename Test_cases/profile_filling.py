import pytest
from selenium import webdriver
from page_objects.account_info import Acc_info_and_billing_address
from page_objects.login_page import Login_page
from utilities.readproperties import ReadConfig
from Test_cases.conftest import setup, browser


class Test_001_profile_update:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    account_name = ReadConfig.get_account_name()
    org_name = ReadConfig.get_org_name()
    phone_num = ReadConfig.get_org_name()
    linkedin_id = ReadConfig.get_linkedin_id()
    website = ReadConfig.get_website()

    def test_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp = Login_page(self.driver)
        self.lp.set_email(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.lp.profile_click()
        self.ai = Acc_info_and_billing_address(self.driver)
        self.ai.click_my_account()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.ai.click_profile_info()
        self.ai.set_account_name(self.account_name)
        self.ai.set_org_name(self.org_name)
        self.ai.set_phone_num(self.phone_num)
        self.ai.set_linkedin_id(self.linkedin_id)
        self.ai.set_time_zone()
        self.ai.set_website_url(self.website)
        self.ai.click_save_button()
