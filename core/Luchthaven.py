from database.DbManager import DbManager
import re

class Luchthaven():

    def init(self):

        self.db_manager = DbManager("Luchthaven.db")

        print("Welkom in de luchthaven applicatie.\n")
        print("1) Bekijk geplande vluchten")
        print("2) Voeg een vlucht toe")
        print("3) Schrap een vlucht")
        print("4) Beëindig sessie\n")

        while True:
            try:
                print("Gelieve een optie te selecteren")
                choice = input("> ").strip()
                if re.match(r'^[1-4]$', choice):
                    match choice:
                        case "1":
                            self.get_flights()
                        case "2":
                            self.add_flight()
                        case "3":
                            self.cancel_flight()
                        case "4":
                            print("\n\nTot ziens!")
                            return;
                else:
                    print("Gelieve een getal tussen 1 en 4 in te vullen.")
            except ValueError:
                print("Gelieve een geldige waarde in te vullen.")

    def get_flights(self):
        output = self.db_manager.get_flights()
        if output is None:
            return "Er werden geen vluchten gevonden"
        else:
            for flight in output:
                print(f"Vlucht {flight.iata_code} van {flight.origin_airport} naar {flight.arrival_airport} is ingepland om {flight.timestamp}.")
        

    def add_flight(self):
        pass

    def cancel_flight(self):
        pass