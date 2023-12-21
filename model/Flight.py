class Flight:

    def __init__(self, iata_code, origin_airport, arrival_airport, timestamp):
        self.iata_code = iata_code
        self.origin_airport = origin_airport
        self.arrival_airport = arrival_airport
        self.timestamp = timestamp


    def get_summary(self):
        return f"Vlucht {self.iata_code} van {self.origin_airport} naar {self.arrival_airport} is ingepland om {self.timestamp}."