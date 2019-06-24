
from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://github.com")
# driver.get("http://smartbear.com")
time.sleep(3)
driver.quit()
