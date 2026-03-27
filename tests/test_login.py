from selenium import webdriver
from pages.login_page import LoginPage
import pytest 

class TestLogin:

    def setup_method(self):
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
   
    def teardown_method(self):
        #runs after every test
        self.driver.quit()

    def test_valid_login(self):
        #with valid credentials
        login=LoginPage(self.driver)
        login.open
        login.enter_username("tomsmith")
        login.enter_password("SuperSecretPassword!")
        login.click_login
        assert "you logged into a secure area" in login.get_success_message()
    def test_invalid_login(self):
        #with invalid credentials
        login = LoginPage(self.driver)
        login.open()
        login.enter_username("wronguser")
        login.enter_password("wrongpassword")
        login.click_login()
        assert "Your username is invalid!" in login.get_error_message()
       