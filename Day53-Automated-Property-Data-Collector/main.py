import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

FORM_URL = "https://forms.gle/APj78fT1iuB8aWiF7"
DATA_SOURCE = "https://appbrewery.github.io/Zillow-Clone"

response = requests.get(url=DATA_SOURCE)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

properties = soup.select(selector="li[class*='StyledListCardWrapper']")

all_listing_details = []

for listing in properties:
    link_element = listing.select_one(selector=".StyledPropertyCardDataWrapper > a")
    link = link_element.get("href")

    price_element = listing.select_one(selector="div > div.StyledPropertyCardDataWrapper > div[class*='StyledPropertyCardDataArea'] > div > span")
    if "+" in price_element.string:
        price = price_element.string.split("+")[0]
    else:
        price = price_element.string.split("/")[0]

    address_element = listing.select_one(selector="address")
    address = address_element.string.strip()

    all_listing_details.append({
        "link": link,
        "price": price,
        "address": address
    })

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 2)


for listing in all_listing_details:

    driver.get(url=FORM_URL)
    time.sleep(1)

    address_input = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_input.clear()
    address_input.send_keys(listing.get("address"))

    price_input = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input.clear()
    price_input.send_keys((listing.get("price")))

    link_input = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input.clear()
    link_input.send_keys((listing.get("link")))

    submit_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span')))
    submit_button.click()

    time.sleep(1)

print("Data entry complete")
driver.quit()
