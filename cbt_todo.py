
from selenium import webdriver
import time

driver = None
try:
	# driver = webdriver.Chrome()
	username = "tonyprod2000@gmail.com"
	authkey  = ""

	caps = {}

	caps['name'] = "Testing - " + time.ctime()
	caps['browser_api_name'] = 'Chrome50'
	caps['os_api_name'] = 'WinVista-C2'
	caps['screen_resolution'] = '1024x768'
	caps['record_video'] = 'true'
	caps['record_network'] = 'false'

	# connect here
	driver = webdriver.Remote(
		desired_capabilities=caps,
		command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(username,authkey)
	)
	
	driver.set_window_size(800,800)
	driver.get('http://crossbrowsertesting.github.io/todo-app.html')

	# how did we find these? INSPECT IN CHROME IS YOUR FRIEND!
	print "Clicking Checkbox"
	driver.find_element_by_name("todo-4").click()
	print "Clicking Checkbox"
	driver.find_element_by_name("todo-5").click()

	print "ABOUT TO ADD AN ITEM"
	time.sleep(2)
	driver.find_element_by_id('todotext').send_keys('Run your first Selenium Test')
	time.sleep(3)
	driver.find_element_by_id('addbutton').click()
	time.sleep(3)
finally:
	if driver is not None:
		driver.quit()