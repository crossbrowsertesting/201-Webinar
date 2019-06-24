
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")

e = driver.find_element_by_name("q")
print e
e.send_keys("cross browser testing")

time.sleep(3)
driver.quit()
