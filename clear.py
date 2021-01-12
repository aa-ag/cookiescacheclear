###--- IMPORTS ---###
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


###--- CODE ---###

browser = webdriver.Chrome()
browser.get("https://reddit.com")
cookies = browser.get_cookies()
for cookie in cookies:
    print(cookie)

browser.quit()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    pass
