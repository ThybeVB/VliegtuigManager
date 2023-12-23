from database.DbManager import DbManager
import re, locale, csv

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

            print("Wil je deze geselecteerde vluchten wegschrijven naar een CSV-bestand? (J/N)")
            csv_keuze = input("> ").strip().lower()
            if re.match(r'^[jn]$', csv_keuze):
                match csv_keuze:
                    case "j":
                        self.generate_csv(output)
                        print("CSV-bestand werd weggeschreven naar Vluchten.csv")
                    case "n":
                        return
            else:
                print("Gelieve een correct argument te geven (J/N)")

    def generate_csv(self, flight_list):
        locale.setlocale(locale.LC_ALL, 'nl_BE.UTF-8')

        try:
            with open('Vluchten.csv', 'w', newline='') as invoice_file:
                writer = csv.writer(invoice_file)
                header = ["IATA Code", "Vliegt vanuit", "Vliegt naar", "Tijdstip"]
                writer.writerow(header)
                for flight in flight_list:
                    flight_record = []
                    flight_record.append(flight.iata_code)
                    flight_record.append(flight.origin_airport)
                    flight_record.append(flight.arrival_airport)
                    flight_record.append(flight.timestamp)
                    writer.writerow(flight_record)
        except Exception as e:
            print("Fout bij wegschrijven: ", e)


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
        print("Je hebt gekozen een vlucht te schrappen.")

        print("Wat is het vluchtnummer?")
        iata_code = input("> ").strip().lower()
        self.db_manager.cancel_flight(iata_code)
        print(f"Vlucht {iata_code.upper()} werd geschrapt.")