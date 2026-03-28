from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.flipkart_page import FlipkartPage
import pytest

class TestFlipkart:

    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self):
        self.driver.quit()

    def test_flipkart_opens(self):
        page = FlipkartPage(self.driver)
        page.open()
        assert "Online Shopping" in self.driver.title
        print("✅ Flipkart opened successfully")

    def test_search_product(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("iPhone 15")
        assert "IPhone" in self.driver.title
        print("✅ Search working correctly")

    def test_search_results_appear(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("Samsung Galaxy")
        count = page.get_results_count()
        assert count > 0
        print(f"✅ Found {count} results")