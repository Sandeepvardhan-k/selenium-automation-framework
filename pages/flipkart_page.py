from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartPage:

    # Locators
    SEARCH_BOX = (By.NAME, "q")
    CLOSE_LOGIN_POPUP = (By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div[data-id]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.flipkart.com")

    def close_login_popup(self):
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable(self.CLOSE_LOGIN_POPUP))
            close_btn.click()
        except:
            pass

    def search_product(self, product):
        search = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_BOX))
        search.clear()
        search.send_keys(product)
        search.send_keys(Keys.ENTER)

    def get_results_count(self):
        results = self.wait.until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULTS))
        return len(results)

    def get_page_title(self):
        return self.driver.title