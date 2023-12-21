class Flight:

    def __init__(self, iata_code, origin_airport, arrival_airport, timestamp):
        self.iata_code = iata_code
        self.origin_airport = origin_airport
        self.arrival_airport = arrival_airport
        self.timestamp = timestamp


    def get_summary(self):
        return "Flight " + self.iata_code + " from " + self.origin_airport + " to " + self.arrival_airport + " at " + self.timestamp + "."