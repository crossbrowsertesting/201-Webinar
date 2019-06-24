"""
starting the login locally
"""

from selenium import webdriver
import time

driver = None
try:
	# driver = webdriver.Chrome()


	username = "johnreese.vt@gmail.com"
	authkey  = ""

	caps = {}

	caps['name'] = "Testing - " + time.ctime()
	caps['browser'] = 'chrome'
	caps['version'] = 'latest'
	caps['platform'] = 'windows'
	caps['record_video'] = 'true'

	# connect here
	driver = webdriver.Remote(
		desired_capabilities=caps,
		command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(username,authkey)
	)

	driver.set_window_size(640,480)
	time.sleep(2)

	driver.get('http://crossbrowsertesting.github.io/login-form.html')

	time.sleep(2)

	driver.find_element_by_name('username').send_keys('tester@crossbrowsertesting.com')
	time.sleep(2)

	driver.find_element_by_name('password').send_keys('test123')
	time.sleep(2)

	driver.find_element_by_css_selector('body > div > div > div > div > form > div.form-actions > button').click()
	time.sleep(2)

finally:
	if driver is not None:
		driver.quit()
