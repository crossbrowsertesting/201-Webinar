
from selenium import webdriver
import time

driver = None
try:
    driver = webdriver.Chrome()
    driver.get("http://crossbrowsertesting.github.io/selenium_example_page.html")
    driver.set_window_size(1024,768)

    print "find an anchor element..."
    e = driver.find_element_by_id("list-test")

    print "look for children underneath the anchor..."
    children = e.find_elements_by_tag_name("li")
    for child in children:
        print "CHILD", child.text

    time.sleep(3)
except:
    # print out exceptions
    import traceback
    traceback.print_exc()
finally:
    if driver is not None:
        driver.quit()

print "all done"
