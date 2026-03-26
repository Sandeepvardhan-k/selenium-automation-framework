from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    def __init__(self):
        self.driver = driver
    USERNAME=(By.CSS_SELECTOR,"#username")
    PASSWORD=(By.CSS_SELECTOR,"#password")
    LOGIN_BTN=(By.CSS_SELECTOR,".radius")
    SUCCESS_MSG=(By.CSS_SELECTOR,".flash.success")
    ERROR_MSG=(By.CSS_SELECTOR,".flash.error")
    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
    def enter_username(self,user):
        self.driver.find_element(*self.USERNAME).send_keys("user")
    def enter_password(self,pwd):
        self.driver.find_element(*self.PASSWORD).send_keys("pwd")
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()
    def get_success_message(self):
        message=self.wait.until(EC.presence_of_element_located(self.SUCCESS_MSG))
        return message.text
    def get_error_message(self):
        error=self.wait.until(EC.presence_of_element_located(self.ERROR_MSG))
        return error.text    