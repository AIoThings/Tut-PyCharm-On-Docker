from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

sleep(5)

# driver = webdriver.Remote("http://selenium:4444/wd/hub")
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
driver.save_screenshot('screenshot.png')
