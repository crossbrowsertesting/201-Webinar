
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://google.com")

time.sleep(1)
e = driver.find_element_by_name("q")
print e
# print dir(e)
driver.quit()
