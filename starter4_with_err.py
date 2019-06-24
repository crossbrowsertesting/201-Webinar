
from selenium import webdriver
import time

driver = None
try:
    driver = webdriver.Chrome()
    driver.get("http://google.com")

    # this line is a typo
    # we meant to find the element q...
    e = driver.find_element_by_name("w")
    print e
    e.send_keys("cross browser testing")

    time.sleep(3)
except:
    # print out exceptions
    import traceback
    traceback.print_exc()
finally:
    if driver is not None:
        driver.quit()

print "all done"
