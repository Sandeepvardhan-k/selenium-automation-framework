from selenium import webdriver
from pages.flipkart import FlipkartPage
from selenium.webdriver.chrome.options import Options
import pytest
 
class TestFlipkart:
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        self.driver=webdriver.Chrome(options=options)
    def teardown_method(self):
        self.driver.quit()
    def test_flipkart_opens(self):
        page=FlipkartPage(self.driver)
        page.open()
        assert "flipkart" in self.driver.title
    def test_search_product(self):
        page=FlipkartPage(self.driver)
        page.open()
        page.close_login_page()
        page.search_product("iphone")
        assert "iphone" in self.driver.title
    def test_search_results_appear(self):
        page=FlipkartPage(self.driver)
        page.open()
        page.close_login_page()
        page.search_product("samsung")
        count= page.get_results_count()
        assert count>0
