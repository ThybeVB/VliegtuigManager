class Flight:

    def __init__(self, iata_code, origin_airport, arrival_airport, timestamp, plane):
        self.iata_code = iata_code
        self.origin_airport = origin_airport
        self.arrival_airport = arrival_airport
        self.timestamp = timestamp
        self.plane = plane


    def get_summary(self):

        if len(self.plane) == 0:
            return f"Vlucht {self.iata_code} van {self.origin_airport} naar {self.arrival_airport} is ingepland om {self.timestamp}."
        else:
            return f"Vlucht {self.iata_code} van {self.origin_airport} naar {self.arrival_airport} is ingepland om {self.timestamp} met vliegtuig {self.plane}."

        