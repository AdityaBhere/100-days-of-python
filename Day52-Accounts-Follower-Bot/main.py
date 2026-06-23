import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = "EXAMPLE"       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = "EXAMPLE"
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 2)

    def login(self):
        self.driver.get(LOGIN_URL)

        email_input = self.wait.until(ec.presence_of_element_located((By.ID, "username")))
        email_input.clear()
        email_input.send_keys(USERNAME)

        password_input = self.wait.until(ec.presence_of_element_located((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(PASSWORD)

        submit_button = self.driver.find_element(By.XPATH, value="//button[contains(text(),'Log in')]")
        submit_button.click()

        dismiss_save_info = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "naan-popup-dismiss")))
        dismiss_save_info.click()

        notifications_button = self.driver.find_element(By.XPATH, value="//button[contains(text(),'Not Now')]")
        notifications_button.click()


    def find_followers(self):
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}/followers")

        modal = self.driver.find_element(By.CSS_SELECTOR, value=".followers-scroll")
        for _ in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)


    def follow(self):
        all_followers = self.driver.find_elements(By.CSS_SELECTOR, value=".naan-follower-row")
        for follower in all_followers:
            follow_button = follower.find_element(By.CSS_SELECTOR, value=".naan-follow-btn")
            try:
                follow_button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()
                time.sleep(0.25)

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()