###--- IMPORTS ---###
import time
from selenium import webdriver


###--- CODE ---###
driver = webdriver.Chrome()
driver.get('http://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name('q')
search_box.send_keys('The Wall Street Journal')
search_box.submit()
time.sleep(5)
driver.quit()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    pass
