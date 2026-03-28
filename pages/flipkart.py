from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartPage:
    #locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CLOSE_LOGIN_POPUP = (By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div._1AtVbE")
    FIRST_RESULT = (By.CSS_SELECTOR, "div._1AtVbE:first-child a")

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def open(self):
        self.driver.get("https://www.flipkart.com")
    def close_login_page(self):
        try:
            close_btn=self.wait.until(EC.element_to_be_clickable(self.CLOSE_LOGIN_POPUP))
            close_btn.click()
        except:
            pass
    def search_product(self,product):
        search=self.wait.until(EC.presence_of_element_located(self.SEARCH_BOX))
        search.send_keys(product)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
    def get_results_count(self):
        results=len(self.wait.until(EC.presence_of_all_elements_located(self.SEARCH_RESULTS)))
    def get_page_title(self):
        return self.driver.title
    
    
      