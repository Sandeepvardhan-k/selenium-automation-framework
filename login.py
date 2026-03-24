from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()          #driver opens url in chrome
driver.maximize_window()           # to maximize thw window of website
try:
    driver.get("https://the-internet.herokuapp.com/login")  #website url
    wait=WebDriverWait(driver,10)  #driver waits 10 seconds , but if the element appears it runs code
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#username")))           #finding element
    driver.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith")              # finding element + action
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("SuperSecretPassword!")  # finding element + action
    driver.find_element(By.CSS_SELECTOR,".radius").click()                              # finding element + action
    message=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".flash.success")))
    m=message.text        #checking if logged into website or not
    if "You logged into a secure area!" in m:
        print("pass")
    else:
        print("fail")
except:
    print("element not found")                  # if element not found it prints "element not found"
finally:
    driver.quit()                  #web driver quits after completing the task