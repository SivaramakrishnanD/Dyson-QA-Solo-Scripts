from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
chromedriver_autoinstaller.install(cwd=True)
driver = webdriver.Chrome()
driver.get('file:///Users/sivaramakrishnand/Desktop/TESTS/CV%20TEST/index.html')
driver.get('file:///Users/sivaramakrishnand/Desktop/TESTS/CV%20TEST/index.html')
sleep(5)
driver.get_screenshot_as_file("screenshot.png")
driver.quit()