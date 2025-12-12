from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

URL = "https://ozh.github.io/cookieclicker/"


driver = webdriver.Firefox()
driver.get(URL)

sleep(2)
try:
    driver.find_element(By.ID, "langSelect-EN").click()
except NoSuchElementException:
    pass

sleep(2)
try:
    driver.find_element(By.CLASS_NAME, "cc_btn").click()
except NoSuchElementException:
    pass

big_cookie = driver.find_element(By.ID, "bigCookie")
