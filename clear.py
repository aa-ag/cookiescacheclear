###--- IMPORTS ---###
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


###--- CODE ---###

browser = webdriver.Chrome()
browser.get("https://google.com")
cookies = browser.get_cookies()
print(browser.get_cookies())
'''
[{'domain': '.google.com', 
'expiry': 1626305828, 
'httpOnly': True, 'name': 
'NID', 'path': '/', 
'sameSite': 'None', 
'secure': True, 
'value': '207=XYn4DD9m_D5T3YqM6-XW8Va01V-oD9IbUabcsT-2hnemYdgjHlavnZv7hl2F5jnFFif4ot5gWZZr9Dt2s9-NKo2q693jUXU0p_zwivQIuzZXqvYWov7IlUO8K3oT9hvMV8Uf1W9gCIsO1JeMknQgHNYZMLC_Q4a19i-TMhxeb-M'}, 
{'domain': '.google.com', 
'expiry': 1613086629, 
'httpOnly': False, 
'name': '1P_JAR', 
'path': '/', 
'sameSite': 
'None', 'secure': True, 'value': '2021-01-12-23'}]
'''

browser.delete_all_cookies()
cookies = browser.get_cookies()
print(browser.get_cookies())
# []

browser.close()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    pass
