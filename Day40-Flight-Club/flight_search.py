import os
from dotenv import load_dotenv
import requests

load_dotenv()
class FlightSearch:
    def __init__(self):
        self.serp_base_url = "https://serpapi.com/search?engine=google_flights"
        self._api_key = os.environ["SERP_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        params = {
            "api_key" : self._api_key,
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time,
            "return_date": to_time,
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "gl": "uk",
            "hl": "en",
            "deep_search": True,
            "show_hidden": True,
        }
        if is_direct:
            params["stops"] = 1

        response_data = requests.get(url=self.serp_base_url, params=params).json()
        if response_data is None or "error" in response_data:
            return requests.get(url=self.serp_base_url, params=params).json()
        return response_data

