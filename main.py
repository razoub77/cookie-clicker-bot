from time import sleep, time

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


def clicking():
    timeout = time() + 5
    while time() < timeout:
        big_cookie.click()


def check_building_upgrades():
    buildings = driver.find_elements(
        By.CSS_SELECTOR, "#products .product.unlocked.enabled"
    )

    if len(buildings) > 0:
        highest_building = buildings[0]
        for building in buildings:
            price = building.find_element(By.CLASS_NAME, "price").text
            highest_price = highest_building.find_element(By.CLASS_NAME, "price").text

            price = int(price.replace(",", ""))
            highest_price = int(highest_price.replace(",", ""))

            if price > highest_price:
                highest_building = building

        highest_building.click()


while True:
    clicking()
    check_building_upgrades()
