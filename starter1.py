
from selenium import webdriver
import time

driver = webdriver.Chrome()

time.sleep(1)
driver.get("http://github.com")

time.sleep(3)
driver.quit()
