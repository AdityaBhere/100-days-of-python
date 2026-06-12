import requests
import os
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_prices_base_url = os.environ["SHEETY_ENDPOINT_PRICES"]
        self.sheety_users_base_url = os.environ["SHEETY_ENDPOINT_USERS"]
        self.headers = {
            "Authorization": f"Basic {os.environ['DATA_MANAGER_AUTH_KEY']}"
        }
        self.price_response = requests.get(url=self.sheety_prices_base_url, headers=self.headers).json()

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self.sheety_prices_base_url}/{row_id}",
            json=new_data,
            headers=self.headers
        )

    def get_customer_emails(self):
        users_response = requests.get(url=self.sheety_users_base_url, headers=self.headers).json()
        email_list = [response["whatIsYourEmail?"] for response in users_response["users"]]
        return email_list
