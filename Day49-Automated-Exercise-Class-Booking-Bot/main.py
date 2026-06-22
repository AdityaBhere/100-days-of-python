import os
import time

from selenium import webdriver
from selenium.common import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

#you should first open the website and register this testing mail
ACCOUNT_EMAIL = "testmail123@gmail.com"
ACCOUNT_PASSWORD = "Testmail@123"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://appbrewery.github.io/gym/")


wait = WebDriverWait(driver,2)


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except (TimeoutException, WebDriverException):
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, value="password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_EMAIL)

    submit_button = driver.find_element(By.ID, value="submit-button")
    submit_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

retry(login, description="login")

def process_booking_action(booking_button, success_text):
    booking_button.click()
    wait.until(lambda d: booking_button.text == success_text)

classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0
total_tue_thu_classes = 0

class_cards = driver.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            total_tue_thu_classes += 1
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            if button.text == "Booked":
                print(f"✓ Already Booked: {class_name.capitalize()} class on {day_title}.")
                already_booked_waitlisted += 1
            elif button.text == "Join Waitlist":
                retry(lambda: process_booking_action(button, "Waitlisted"), description="Joining Waitlist")
                waitlists_joined += 1
                print(f"✓ Joined Waitlist for: {class_name.capitalize()} class on {day_title}.")
                time.sleep(0.5)
            elif button.text == "Waitlisted":
                already_booked_waitlisted += 1
                print(f"✓ Already on waitlist: {class_name.capitalize()} class on {day_title}.")
            elif button.text == "Book Class":
                retry(lambda: process_booking_action(button, "Booked"), description="Booking Class")
                classes_booked += 1
                print(f"✓ Successfully booked: {class_name.capitalize()} class on {day_title}")
                time.sleep(0.5)


def get_my_bookings_cards():
    my_bookings_button = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_button.click()
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
    confirmed = driver.find_elements(By.CSS_SELECTOR, value="div[id^='booking-card-booking']")
    waitlisted = driver.find_elements(By.CSS_SELECTOR, value="div[id^='waitlist-card-waitlist']")
    all_booking_cards = confirmed + waitlisted
    if not all_booking_cards:
        raise TimeoutException("No booking cards found")
    return all_booking_cards


expected_total = already_booked_waitlisted + classes_booked + waitlists_joined
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_tue_thu_classes} ---\n")
print("--- VERIFYING ON MY BOOKINGS PAGE ---")

verified_cards = retry(get_my_bookings_cards, description="Get my bookings page cards")
verified_count = 0

for card in verified_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_title = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_title.capitalize()}")
            verified_count += 1
    except NoSuchElementException:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {expected_total} bookings")
print(f"Found: {verified_count} bookings")

if expected_total == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {expected_total - verified_count} bookings")
