from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from time import sleep

INSTA_USERNAME = os.environ["INSTA_USERNAME"]
INSTA_PSWD = os.environ["INSTA_PSWD"]
chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
# driver.maximize_window()
driver.get("https://www.instagram.com/")
sleep(2)

enter_username = driver.find_element("name", "username")
enter_username.send_keys(INSTA_USERNAME)
enter_pswd = driver.find_element("name", "password")
enter_pswd.send_keys(INSTA_PSWD)
login = driver.find_element("css selector", "._acan div")
login.click()
sleep(8)

driver.get("https://www.instagram.com/_javadeveloper/?next=%2F#")
sleep(4)
followers = driver.find_element("css selector", "li a")
followers.click()
sleep(4)

follow_btns = driver.find_elements("css selector", "._aano button")
for btn in follow_btns:
    btn.click()
