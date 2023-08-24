
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class Login_page:
    #class attribute
    email_textbox_id = "email-id"
    password_textbox_id = "password"
    login_button_xpath = "//button[@type='submit']//span[@class='MuiButton-label']"
    profile_element_xpath = "//img[@class='img-align-radius']"
    logout_button_xpath = "//img[@class='img-align-radius']"

    # constructed, it can be used when we create a class instances
    def __init__(self, driver):
        self.driver = driver
#set_email is a method, and username is parameter and self also a parameter
    def set_email(self, username):
        email_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.email_textbox_id)))
        email_element.clear()
        email_element.send_keys(username)


    def set_password(self, password):
        password_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self. password_textbox_id)))
        password_element.clear()
        password_element.send_keys(password)

    def login_click(self):
         login_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.login_button_xpath)))
         login_element.click()


    def profile_click(self):

        profile_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.profile_element_xpath)))
        profile_element.click()

    def logout_click(self):
        logout_element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.logout_button_xpath)))
        logout_element.click()

