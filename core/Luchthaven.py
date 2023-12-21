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
                            print("\nTot ziens!")
                            self.db_manager.close_connection()
                            return
                else:
                    print("Gelieve een getal tussen 1 en 4 in te vullen.")
            except ValueError:
                print("Gelieve een geldige waarde in te vullen.")

    def get_flights(self):
        output = self.db_manager.get_flights()
        if output is None:
            print("Er werden geen vluchten gevonden\n")
        else:
            for flight in output:
                print(flight.get_summary())
        

    def add_flight(self): #todo: add nullchecks en validatie
        print("Je hebt gekozen een vlucht toe te voegen.")
        
        print("Wat is het vluchtnummer?")
        iata_code = input("> ").strip()

        print("Wat is de vertrekluchthaven? (Standaard: BRU)")
        origin_airport = input("> ").strip().upper()

        print("Wat is de luchthaven van aankomst?")
        arrival_airport = input("> ").strip().upper()

        print("Om hoelaat vertrekt de vlucht?")
        timestamp = input("> ").strip()

        if len(origin_airport) == 0:
            origin_airport = "BRU"

        self.db_manager.add_flight(iata_code, origin_airport, arrival_airport, timestamp)
        print("Vlucht toegevoegd!\n")

    def cancel_flight(self):
        pass