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
        print("Flipkart opened successfully")

    def test_search_product(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("iPhone 15")
        assert "IPhone" in self.driver.title
        print("Search working correctly")

    def test_search_results_appear(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("Samsung Galaxy")
        count = page.get_results_count()
        assert count > 0
        print(f"Found {count} results")
    def test_product_price_exists(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("iPhone 15")
        price = page.get_first_product_price()
        assert "₹" in price
        print(f"First product price: {price}")
    def test_search_url_changes(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()
        page.search_product("laptop")
        current_url = page.get_current_url()
        assert "laptop" in current_url.lower()
        print(f"URL updated correctly: {current_url}")
    def test_search_box_accepts_input(self):
        page = FlipkartPage(self.driver)
        page.open()
        page.close_login_popup()        
        search_box = self.driver.find_element(*page.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys("Samsung")
        value = page.get_search_box_value()
        assert "Samsung" in value
        print(f"Search box contains: {value}")