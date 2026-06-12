import requests_cache
from data_manager import DataManager
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from flight_search import FlightSearch

requests_cache.install_cache()

day_after_12_days = str((datetime.now() + timedelta(days=12)).date())
month_from_today = str((datetime.now() + timedelta(days=30)).date())


sheet_manager = DataManager()
price_data = sheet_manager.price_response["prices"]

flight_checker = FlightSearch()

ORIGIN_CITY_IATA = "LHR"

for destination in price_data:
    pprint(f"Getting flights for {destination['city']}")

    flights = flight_checker.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=day_after_12_days,
        to_time=month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=month_from_today)

    if cheapest_flight.price == "N/A":
        pprint(f"No direct flight to {destination['city']}. Looking for indirect flights")

        stopover_flights = flight_checker.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=day_after_12_days,
            to_time=month_from_today,
            is_direct=False
        )

        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=month_from_today)
        pprint(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        sheet_manager.update_lowest_price(destination["id"], cheapest_flight.price)

        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only GBP {cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"with {cheapest_flight.stops} stop(s) "
                f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
            )
        print(message)
