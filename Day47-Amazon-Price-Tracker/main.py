from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

header = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "your user-agent"
}

product_url = "product you want to track"
response = requests.get(url=product_url, headers=header)
site_html = response.text

soup = BeautifulSoup(site_html, "html.parser")

product_name = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip()

# this split of before and after comma is required as the prices on amazon.in are seperated by ,
product_price_before_comma = soup.find(name="span", class_="a-price-whole").getText().split(",")[0]
product_price_after_comma = soup.find(name="span", class_="a-price-whole").getText().split(",")[1].strip(".")
product_price = int(product_price_before_comma + product_price_after_comma)

desired_price = "required price"

my_email = os.environ["EMAIL_ADDRESS"]
password = os.environ["EMAIL_PASSWORD"]

if product_price < desired_price:
    with smtplib.SMTP(host=os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= "receivers mail address",
            msg=f"Subject:Amazon Price Alert\n\n{product_name} is now ₹{product_price}.\n{product_url}")
        print("mail sent successfully...")
