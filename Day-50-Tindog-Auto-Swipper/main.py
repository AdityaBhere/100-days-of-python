import time
import os
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

tindog_url = "add your own tindog url from https://app.100daysofpython.dev/"
driver.get(url=tindog_url)

facebark_email = "abc123@gmail.com"   #example mail
facebark_password = "Abc@123"         #exampe password

wait = WebDriverWait(driver, 2)

login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-tindog-login']")))
login_button.click()

facebark_login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button[class^='btn-facebark']")))
facebark_login_button.click()

base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]

driver.switch_to.window(facebark_window)

email_input = wait.until(ec.presence_of_element_located((By.ID, "email")))
email_input.clear()
email_input.send_keys(facebark_email)

password_input = wait.until(ec.presence_of_element_located((By.ID, "pass")))
password_input.clear()
password_input.send_keys(facebark_password)

submit_button = driver.find_element(By.XPATH, value="/html/body/div[2]/div/form/button")
submit_button.click()

driver.switch_to.window(base_window)


allow_location_button = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
allow_location_button.click()

notifications_button = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "btn-secondary")))
notifications_button.click()

time.sleep(0.5)
allow_cookies_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "body > main > div > div > form > button")))
allow_cookies_button.click()

daily_swipe_limit = 20

for i in range(1, daily_swipe_limit):
    try:
        time.sleep(1)
        tick_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="like-button-container"]/form/button')))
        tick_button.click()
    except ElementClickInterceptedException:
        back_to_tindog_button = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/div[3]/a')))
        back_to_tindog_button.click()
