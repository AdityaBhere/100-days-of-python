import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PROMISED_DOWN = 100
PROMISED_UP = 100
Y_EMAIL = "your registered email"
Y_PASSWORD = "your password"
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 2)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        start_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[class='start-text']")))
        start_button.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[4]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text



    def tweet_at_provider(self):
        url = Y_LOGIN_URL
        self.driver.get(url)
        email_input = self.wait.until(ec.presence_of_element_located((By.ID, "email")))
        email_input.clear()
        email_input.send_keys(Y_EMAIL)

        password_input = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(Y_PASSWORD)

        submit_button = self.driver.find_element(By.XPATH, value="/html/body/div/div/form/button")
        submit_button.click()

        message_to_post = f"Hey Internet Provider, why is my speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?!"
        post_input =  self.wait.until(ec.presence_of_element_located((By.ID, "tweet-compose")))
        post_input.clear()
        post_input.send_keys(message_to_post)

        post_button =self.wait.until(ec.element_to_be_clickable((By.ID, "post-btn")))
        post_button.click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()