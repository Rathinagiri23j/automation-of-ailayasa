from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Acc_info_and_billing_address:
    # these are the class attributes
    email_textbox_id = "email-id"
    password_textbox_id = "password"
    login_button_xpath = "//button[@type='submit']//span[@class='MuiButton-label']"
    lst_my_account_xpath = "//a[normalize-space()='My account']"
    href_profile_info_xpath = "//div[@class='sidebar-links-cont']//div[1]//ul[1]//li[1]"
    txt_primary_account_name_xpath = "//div[@class='collapse show']//input[@id='name']"
    txt_organization_name_xpath = "//input[@id='text']"
    txt_phone_xpath = "//input[@id='phone']"
    txt_linkedin_xpath = "//input[@id='linked_id']"
    cb_time_zone_xpath = "//div[@class='collapse show']//div[@class=' css-1hwfws3']"
    opt_india_time_xpath = "//div[contains(text(),'UTC+05:30 - Indian Standard Time')]"
    txt_website_xpath = "//input[@id='website']"
    btn_save_xpath = "//div[@class='collapse show']//button[@class='setting-frm-button'][normalize-space()='Save']"

    def __init__(self, driver):
        self.driver = driver

    def click_my_account(self):
        # we have used only one explicit wait because if the first one is visible then rest of the element also get to visible.
        my_account_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lst_my_account_xpath)))
        my_account_element.click()

    def click_profile_info(self):
        profile_click= self.driver.find_element(By.XPATH, self.href_profile_info_xpath)
        profile_click.click()

    def set_account_name(self, account_name):
        # we have used only one explicit wait because if the first one is visible then rest of the element also get to visible.
        account_name_element = self.driver.find_element(By.XPATH, self.txt_primary_account_name_xpath)
        account_name_element.clear()
        account_name_element.send_keys(account_name)

    def set_org_name(self, org_name):
        org_name_element = self.driver.find_element(By.XPATH, self.txt_organization_name_xpath)
        org_name_element.clear()
        org_name_element.send_keys(org_name)

    def set_phone_num(self, phone_num):
        phone_number_element = self.driver.find_element(By.XPATH, self.txt_phone_xpath)
        phone_number_element.clear()
        phone_number_element.send_keys(phone_num)

    def set_linkedin_id(self, linkedin_id):
        linked_in_element = self.driver.find_element(By.XPATH, self.txt_linkedin_xpath)
        linked_in_element.send_keys(linkedin_id)

    def set_time_zone(self):
        country_element = self.driver.find_element(By.XPATH, self.cb_time_zone_xpath)
        country_element.click()
        time.sleep(3)
        india_element = self.driver.find_element(By.XPATH, self.opt_india_time_xpath)
        india_element.click()

    def set_website_url(self, website):
        website_element = self.driver.find_element(By.XPATH, self.txt_website_xpath)
        website_element.clear()
        website_element.send_keys(website)

    def click_save_button(self):
        save_button = self.driver.find_element(By.XPATH, self.btn_save_xpath)
        save_button.click()
