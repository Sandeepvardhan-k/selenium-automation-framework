from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self):
        self.driver = driver
    username=(By.CSS_SELECTOR,"#username")
    password=(By.CSS_SELECTOR,"#password")
    login=(By.CSS_SELECTOR,".radius")
    def enter_username(self,user):
        self.driver.find_element(*self.username).send_keys("user")
    def enter_password(self,pwd):
        self.driver.find_element(*self.password).send_keys("pwd")
    def click_login(self):
        self.driver.find_element(*self.login).click()
    def login(self,user,pwd):
        self.enter_username(user)
        self.enter_password(pwd)
        self.click_login()