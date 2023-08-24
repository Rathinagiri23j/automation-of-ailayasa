

from pynput.keyboard import Key, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Project_creation:
    # these are the class attributes
    btn_new_project = "//span[normalize-space()='New project']"
    tab_all = "//li[normalize-space()='All']"
    tab_translation = "//li[normalize-space()='Translation']"
    tab_transcription = "//li[normalize-space()='Transcription']"
    tab_ai_voice = "//li[normalize-space()='AI Voice']"
    tab_assets = "//li[normalize-space()='Assets']"
    tab_toolkit = "//li[normalize-space()='Toolkit']"
    tab_writing = "//li[normalize-space()='Writing']"

    # inside translation_tab
    box_translate_document = "//body/div[@id='root']/div[@id='body-wrap']/div[@class='ai-new-project-setup-wrapper']/div[@class='ai-working-col-wrapper']/section[@class='all-template-glb-wrapper']/div[@class='all-templates-container']/div[@class='all-templates-tab-wrapper']/div[@class='templates-box-list-wrapper']/div[@class='tempalte-boxes-container-wrapper']/div[@class='templates-box-row']/div[2]/div[2]"

    # inside translate files
    txt_project_name = "//div[@class='project-box']"
    link_browse = "//label[normalize-space()='browse']"
    file_input = "//input[@type='file']"
    dd_source_language = "//body/div[@id='root']/div[@id='body-wrap']/div[@class='ai-new-project-setup-wrapper']/div[@class='ai-working-col-wrapper']/div[@class='ai-working-area-glb-wrapper']/div[@class='ai-translate-file-wrapper']/div[@class='project-setup-forms new-file-proj-setup-wrapper file-upload-form']/div[contains(@class,'d-flex gap-3 files-space-align')]/div[1]/div[1]/div[1]/i[1]"
    dd_target_language = "//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]"
    txt_translate_files = "//span[normalize-space()='Translate files']"
    # source language popup
    li_source_english = "//li[normalize-space()='English']"
    # target _language popup
    li_target_tamil = "//li[normalize-space()='Tamil']"
    btn_add_xpath = "//span[@class='login-btn new-padd-style']"
    # advance_settings
    str_checkbox_advance_settings = "//input[@id='advance-setting']"
    str_checkbox_apply_machine_translation = "//label[normalize-space()='Advanced settings']"
    # create button
    btn_create = "//button[@type= 'submit']"
    # my projects page dash_board
    project_info_at_dashboard = "//div[@class='file-edit-list-table-row focused-proj-row']//div[@class='proj-information']"
    project_download_dashboard = "//div[@class='file-edit-list-table-row focused-proj-row']//span[@aria-label='Download']"
    task_file_open = "//body/div[@id='root']/div[@id='body-wrap']/section[@class='padding-correction']/div[@class='tab-content setup-container']/div[@class='tab-pane active']/div[@class='upload-files-section']/div[@id='select-files']/div[@class='file-edit-heading-row project-list-main']/div[@class='file-edit-heading-table']/div[@class='file-edit-list-table-row focused-proj-row']/div[@class='selected-file-row collapse show']/div/div[@class='file-edit-inner-table']/div[@class='file-edit-list-inner-table-row']/div[@class='file-edit-list-inner-table-cell']/div[@class='project-list-action-wrap']/button[1]"

    # transeditor
    btn_download_word = "//div[@class='download-grp-wrapper']"
    my_project_back_button = "//span[normalize-space()='My projects']"

    def __init__(self, driver):

        self.driver = driver


    def click_btn_new_project(self):
        click_btn_new_project_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_new_project)))
        click_btn_new_project_element.click()

    def click_tab_translation(self):
        click_tab_translation_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.tab_translation)))
        click_tab_translation_element.click()

    def click_box_translate_document(self):
        self.driver.find_element(By.XPATH, self.box_translate_document).click()

    def set_project_name(self, project_name):
        txt_project_name_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_project_name)))
        txt_project_name_element.send_keys(project_name)

    def click_browse_text(self):
        upload_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_browse)))
        upload_element.click()

    def key_control_upload(self, file_path):
        keyboard = Controller()
        keyboard.type(file_path)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def click_dd_source_language(self):
        self.driver.find_element(By.XPATH, self.dd_source_language).click()

    def click_li_source_english(self):
        li_source_english_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.li_source_english)))
        li_source_english_element.click()

    def click_dd_target_language(self):
        self.driver.find_element(By.XPATH, self.dd_target_language).click()

    def click_li_target_tamil(self):
        li_target_tamil_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.li_target_tamil)))
        li_target_tamil_element.click()

    def click_btn_add_xpath(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def click_str_checkbox_advance_settings(self):
        self.driver.find_element(By.XPATH, self.str_checkbox_advance_settings)

    def click_str_apply_machine_translation(self):
        str_checkbox_apply_machine_translation_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.str_checkbox_apply_machine_translation)))
        str_checkbox_apply_machine_translation_element.click()

    def click_btn_create(self):
        self.driver.find_element(By.XPATH, self.btn_create).click()

    def click_project_download_dashboard(self):
        project_download_dashboard_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.project_download_dashboard)))
        project_download_dashboard_element.click()

    def click_task_file_open(self):
        self.driver.find_element(By.XPATH, self.task_file_open).click()

    def click_btn_download_word(self):
        btn_download_word_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_download_word)))
        btn_download_word_element.click()

    def click_project_back_button(self):
        self.driver.find_element(By.XPATH, self.my_project_back_button).click()
