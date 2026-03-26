from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLogin:

    def setup_method(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()                  #to maximize window of website
        self.wait = WebDriverWait(self.driver, 10)     #this line tells webdriver to wait 0-10sec for an element
   
    def teardown_method(self):
        #runs after every test
        self.driver.quit()

    def test_valid_login(self):
        #with valid credentials
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))            #waits untill username block appears on page
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")               #action("types username given")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")   #action(types password given)
        self.driver.find_element(By.CSS_SELECTOR, ".radius").click()                               #action(clicks login button)
        message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
        assert "You logged into a secure area!" in message.text    #checks if given text is there in message, if yes "pass" else "fail"

    def test_invalid_login(self):
        #with invalid credentials
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("wronguser")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("wrongpassword")
        self.driver.find_element(By.CSS_SELECTOR, ".radius").click()
        message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error")))
        assert "Your username is invalid!" in message.text