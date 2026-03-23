from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR,".radius").click()
time.sleep(1)
print(driver.title)
try:
    message=driver.find_element(By.CSS_SELECTOR,".flash.success").text
    if "You logged into a secure area!" in message:
        print("pass")
    else:
        print("fail")
except:
    print("element not found")
    
time.sleep(2)
driver.quit()