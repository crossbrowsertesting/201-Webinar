from selenium import webdriver
import time

# Create the webdriver instance
# run test locally against chrome
driver = webdriver.Chrome()


# run test in CBT:
# driver = webdriver.Remote(
#         command_executor = "https://hub.crossbrowsertesting.com/wd/hub",
#         desired_capabilities = { "browser": "chrome",
#                                  "version": "latest",
#                                  "platform": "windows",
#                                  # "deviceName": "Pixel 3",
#                                  "username": "johnreese.vt@gmail.com",
#                                  "password": "u0af4e32dc4fb29d",
#                                  "recordVideo": True})

# navigate
driver.get("https://example.com")
driver.get("https://card-layout.glitch.me/")

# browser nav actions
driver.back()
driver.forward()
driver.refresh()

print "setting size + pos"
driver.set_window_rect(0, 0, 325, 900)
time.sleep(1)

driver.set_window_rect(0, 0, 768, 800)
time.sleep(1)

driver.set_window_rect(0, 0, 1024, 800)
time.sleep(1)

for i in range(325, 1300, 50):
    driver.set_window_rect(0, 0, i, 800)

time.sleep(2)

driver.quit()

