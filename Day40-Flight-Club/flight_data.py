class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    if data is None or "error" in data:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    best_flights = data.get("best_flights", [])
    other_flights = data.get("other_flights", [])

    all_flights = best_flights + other_flights

    if not all_flights:
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")


    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    nr_stops = len(first_flight["flights"]) - 1

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    for flight in all_flights:
        try:
            current_price = flight["price"]
        except KeyError:
            continue

        if current_price < lowest_price:
            lowest_price = current_price
            origin = flight["flights"][0]["departure_airport"]["id"]
            destination = flight["flights"][-1]["arrival_airport"]["id"]
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            nr_stops = len(flight["flights"]) - 1

            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is GBP {lowest_price}")

    return cheapest_flight