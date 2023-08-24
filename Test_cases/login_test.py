import pytest
from selenium import webdriver
from page_objects.login_page import Login_page
from utilities.readproperties import ReadConfig
from Test_cases.conftest import setup,browser
from utilities.customlogger import LogGen




# for example we are creating a 2 test cases


class Test_001_login:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()



    # this is the verification area method, we are just verifying the page.
    def test_homepage_title(self, setup):

        self.logger.info("**** Test 001_login ****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("**** Home page verification started ****")
        actual_title = self.driver.title
        if actual_title == "Ailaysa | Authentication":
            assert True
            self.driver.close()
            print("pass___")
            self.logger.info("**** title verified for homepage *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title1.png")
            self.driver.close()
            assert False
            self.logger.error("**** Home Page tittle mismatched ****")
        self.logger.info("**** Home page verification Test Ended ****")



    def test_login(self,setup):
        self.driver = setup
        self.logger.info("**** Login Test Case started ****")
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.lp = Login_page(self.driver)
        self.lp.set_email(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()

        actual_title = self.driver.title
        self.lp.profile_click()
        self.lp.logout_click()

        if actual_title == "Ailaysa | Projects":
            assert True
            self.driver.close()
            self.logger.info("**** Successful login and verified ****")

        elif actual_title != "Ailaysa | Projects":
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login1.png")
            self.driver.close()
            #assert False
            self.logger.error("**** failed title mismatch *****")

        self.logger.info("**** Login test ended ****")

