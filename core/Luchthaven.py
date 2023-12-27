from database.DbFlight import DbFlight
from database.DbPlane import DbPlane
import re, locale, csv

class Luchthaven():

    def initialize(self, db_file):
        self.db_flights = DbFlight(db_file)
        self.db_planes = DbPlane(db_file)

        print("Welkom in de luchthaven applicatie.\n")

        print("--- Vluchten ---")
        print("1) Bekijk geplande vluchten")
        print("2) Voeg een vlucht toe")
        print("3) Bewerk een vlucht")
        print("4) Schrap een vlucht\n")

        print("--- Toestellen ---")
        print("5) Bekijk de toestellen")
        print("6) Voeg een toestel toe")
        print("7) Bewerk een toestel")
        print("8) Verwijder een toestel\n")

        print("9) Beëindig sessie")

        while True:
            try:
                print("Gelieve een optie te selecteren")
                choice = input("> ").strip()
                if re.match(r'^[1-9]$', choice):
                    match choice:
                        case "1":
                            self.get_flights()
                        case "2":
                            self.add_flight()
                        case "3":
                            self.modify_flight()
                        case "4":
                            self.cancel_flight()
                        case "5":
                            self.get_planes()
                        case "6":
                            self.add_plane()
                        case "7":
                            self.modify_plane()
                        case "8":
                            self.remove_plane()
                        case "9":
                            print("\nTot ziens!")
                            self.db_flights.close_connection()
                            return
                else:
                    print("Gelieve een getal tussen 1 en 9 in te vullen.")
            except ValueError:
                print("Gelieve een geldige waarde in te vullen.")

    def get_flights(self):
        output = self.db_flights.get_flights()
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
                header = ["IATA Code", "Vliegt vanuit", "Vliegt naar", "Vliegtuig", "Tijdstip"]
                writer.writerow(header)
                for flight in flight_list:
                    flight_record = []
                    flight_record.append(flight.iata_code)
                    flight_record.append(flight.origin_airport)
                    flight_record.append(flight.arrival_airport)
                    flight_record.append(flight.plane)
                    flight_record.append(flight.timestamp)
                    writer.writerow(flight_record)
        except Exception as e:
            print("Fout bij wegschrijven: ", e)

    def print_available_planes(self):
        print("\n--- Beschikbare Toestellen ---")
        planes = self.db_planes.get_planes()
        if planes is not None:
            for plane in planes:
                print(plane.get_summary())

    def add_flight(self):
        print("Je hebt gekozen een vlucht toe te voegen.")
        planes = self.db_planes.get_planes()
        if planes is None:
            print("Er werden geen vliegtuigen gevonden die aan deze vlucht gekoppeld kunnen worden. Wil je als nog de vlucht toevoegen? (J/N)")
            keuze = input("> ").strip().lower()
            if keuze == "n":
                print("Toevoegen vlucht afgebroken.\n")
                return
        
        print("Wat is het vluchtnummer?")
        iata_code = input("> ").strip()

        self.print_available_planes()
        print("\nWat is de registratie van het vliegtuig? Hierboven werd een lijst gedrukt met de beschikbare toestellen.")
        plane_reg = ""
        while not self.db_planes.get_plane(plane_reg):
            plane_reg = input("> ").strip().upper()
            if not self.db_planes.get_plane(plane_reg):
                print("Deze registratie werd niet gevonden in de beschikbare vliegtuigen. Vul een registratie uit de lijst in.")

        print("Wat is de vertrekluchthaven? (Standaard: BRU)")
        origin_airport = input("> ").strip().upper()

        print("Wat is de luchthaven van aankomst?")
        arrival_airport = input("> ").strip().upper()

        print("Om hoelaat vertrekt de vlucht?")
        timestamp = input("> ").strip()

        if len(origin_airport) == 0:
            origin_airport = "BRU"

        self.db_flights.add_flight(iata_code, origin_airport, arrival_airport, timestamp, plane_reg)
        print("Vlucht toegevoegd!\n")

    def cancel_flight(self):
        print("Je hebt gekozen een vlucht te schrappen.")

        print("Wat is het vluchtnummer?")
        iata_code = input("> ").strip().lower()
        self.db_flights.cancel_flight(iata_code)
        print(f"Vlucht {iata_code.upper()} werd geschrapt.")

    def get_planes(self):
        output = self.db_planes.get_planes()
        if output is None:
            print("Er werden geen vliegtuigen gevonden\n")
        else:
            for plane in output:
                print(plane.get_summary()) #todo: csv

    def add_plane(self):
        print("Je hebt gekozen een vliegtuig toe te voegen.")

        print("Wat is de registratie van het toestel?")
        registration = input("> ").strip()

        print("Wat is de model van het toestel?")
        type = input("> ").strip()

        print("Tot welke vluchtmaatschappij behoort het toestel?")
        airline = input("> ").strip()

        self.db_planes.add_plane(registration, type, airline)
        print("Vliegtuig toegevoegd!\n")

    def modify_plane(self):
        print("Je hebt gekozen een vliegtuig aan te passen.")

        self.print_available_planes()

        print("Wat is de registratie van het toestel die je wil aanpassen?")
        plane_reg = ""
        while not self.db_planes.get_plane(plane_reg):
            plane_reg = input("> ").strip().upper()
            if not self.db_planes.get_plane(plane_reg):
                print("Deze registratie werd niet gevonden in de beschikbare vliegtuigen. Vul een registratie uit de lijst in.")

        plane = self.db_planes.get_plane(plane_reg)
        print("Om huidige informatie te behouden, druk je op ENTER.")
        
        print(f"New type ({plane.type}):")
        newType = input("> ").strip().upper()
        if not len(newType):
            newType = plane.type

        print(f"New airline ({plane.airline}):")
        newAirline = input("> ").strip()
        if not len(newAirline):
            newAirline = plane.airline

        self.db_planes.modify_plane(plane_reg, newType, newAirline)
        print("Vliegtuig gewijzigd!\n")

    def modify_flight(self):
        print("Je hebt gekozen een vlucht aan te passen.")

        flights = self.db_flights.get_flights()
        if flights is None:
            print("Er zijn geen vluchten om aan te passen.")
            return
        else:
            for flight in flights:
                print(flight.get_summary())

        print("Wat is het vluchtnummer van de vlucht die je wil aanpassen?")
        iata = ""
        while not self.db_flights.get_flight(iata):
            iata = input("> ").strip().upper()
            if not self.db_flights.get_flight(iata):
                print("Deze vlucht werd niet gevonden in de beschikbare vluchten. Vul een IATA-code uit de lijst in.")

        flight = self.db_flights.get_flight(iata)
        print("Om huidige informatie te behouden, druk je op ENTER.")
        
        print(f"Nieuwe vertrekluchthaven ({flight.origin_airport}):")
        new_origin = input("> ").strip()
        if not len(new_origin):
            new_origin = flight.origin_airport

        print(f"Nieuwe bestemmingsluchthaven ({flight.arrival_airport}):")
        new_arrival = input("> ").strip()
        if not len(new_arrival):
            new_arrival = flight.arrival_airport

        print(f"Nieuwe vertrektijd ({flight.timestamp}):")
        new_timestamp = input("> ").strip()
        if not len(new_timestamp):
            new_timestamp = flight.timestamp

        self.print_available_planes()
        print(f"Nieuw vliegtuig ({flight.plane}):")
        plane_reg = ""
        while not self.db_planes.get_plane(plane_reg):
            plane_reg = input("> ").strip().upper()
            if not len(plane_reg):
                plane_reg = flight.plane
            if not self.db_planes.get_plane(plane_reg):
                print("Deze registratie werd niet gevonden in de beschikbare vliegtuigen. Vul een registratie uit de lijst in.")

        self.db_flights.modify_flight(iata, new_origin, new_arrival, new_timestamp, plane_reg)
        print("Vliegtuig gewijzigd!\n")         
    
    def remove_plane(self):
        print("Je hebt gekozen een toestel te schrappen uit de luchthaven.")

        print("Wat is de registratie van het toestel?")
        registration = input("> ").strip().upper()
        self.db_planes.remove_plane(registration)
        print(f"Toestel {registration.upper()} werd geschrapt.")