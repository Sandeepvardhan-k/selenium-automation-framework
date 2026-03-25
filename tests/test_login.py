from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestLogin:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.wait=WebDriverWait(driver,10)
    def teardown_method(self):
        self.driver.quit()
    def test_valid_login(self):
        #with correct credentials
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#username")))
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith")
        self.driver.find_element(By.CSS_SELECTOR,"password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CSS_SELECTOR,".radius").click()
        message=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".flash.success")))
        assert "you logged into a secure area!" in message.text
    def test_invalid_login(self):
        #with wrong credentials
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#username")))
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys("wronguser")
        self.driver.find_element(By.CSS_SELECTOR,"password").send_keys("SuperSecretPsword!")
        self.driver.find_element(By.CSS_SELECTOR,".radius").click()
        message=self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".flash.success")))
        assert "you logged into a secure area!" in message.text


    
    