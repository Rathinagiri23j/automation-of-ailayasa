import time

import pytest
from selenium import webdriver
from page_objects.login_page import Login_page
from utilities.readproperties import ReadConfig
from page_objects.project_creation import Project_creation
from utilities.customlogger import LogGen


class Test_002_project_flow:
    baseurl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_password()
    txt_project_name = ReadConfig.get_project_name()
    file_path = ReadConfig.get_file_path()
    logger = LogGen.loggen()

    def test_project_creation(self, setup):
        self.logger.info("**** Test_002_project_flow starter ****")
        self.driver = setup
        setup.get(self.baseurl)
        setup.implicitly_wait(8)
        setup.maximize_window()
        self.logger.info("**** successfully launched website ****")
        self.lp = Login_page(self.driver)
        self.pg = Project_creation(self.driver)
        self.lp.set_email(self.username)
        self.lp.set_password(self.password)
        self.lp.login_click()
        self.pg.click_btn_new_project()
        self.pg.click_tab_translation()
        self.pg.click_box_translate_document()
        self.pg.set_project_name(self.txt_project_name)
        self.driver.save_screenshot(".\\Screenshots\\" + "project_creation.png")
        self.pg.click_browse_text()
        time.sleep(5)
        self.pg.key_control_upload(self.file_path)
        # self.pg.select_file_for_upload(self.file_path)
        self.pg.click_dd_source_language()
        self.driver.save_screenshot(".\\Screenshots\\" + "project_creation.png")
        self.pg.click_li_source_english()
        self.pg.click_dd_target_language()
        self.driver.save_screenshot(".\\Screenshots\\" + "project_creation22.png")

        self.pg.click_li_target_tamil()
        self.pg.click_btn_add_xpath()
        self.driver.save_screenshot(".\\Screenshots\\" + "project_creation22.png")
        self.pg.click_str_checkbox_advance_settings()
        self.pg.click_str_apply_machine_translation()
        time.sleep(5)
        self.pg.click_btn_create()

        self.pg.click_project_download_dashboard()
        time.sleep(5)
        self.pg.click_task_file_open()
        time.sleep(5)
        self.pg.click_btn_download_word()
        self.pg.click_project_back_button()
