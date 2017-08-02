# encoding:UTF-8
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

file_path = 'num.txt'
with open(file_path) as file_object:
    id = file_object.read()

browser = webdriver.Firefox()

browser.get("http://oa.tiexinba.net/UserLogin.asp")
name=input('name')
key=input('key')
browser.find_element_by_id("UserName").send_keys(name)
browser.find_element_by_id("Password").send_keys(key)
time.sleep(3)  # 休眠3秒
browser.find_element_by_id("Password").send_keys(Keys.ENTER)


time.sleep(3)  # 休眠3秒
#browser.find_element_by_id("Submit").click()
#browser.quit()
url="http://oa.tiexinba.net/ShowArticle.asp?ArticleID="+str(id)
browser.get(url)


