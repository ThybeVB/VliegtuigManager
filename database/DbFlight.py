from model.Flight import Flight
from database.DbManager import DbManager

class DbFlight(DbManager):
    
    def __init__(self, db_file):
        super().__init__(db_file)

    # todo: uitbreiden met zoeken op datum, bestemming
    def get_flights(self, origin_airport=None, arrival_airport=None):
        try:
            query = ""
            if origin_airport is None and arrival_airport is None:
                query = '''SELECT * FROM flights'''
            elif origin_airport is not None and arrival_airport is None:
                query = f"SELECT * FROM flights WHERE origin_airport={origin_airport}"
            elif origin_airport is None and arrival_airport is not None:
                query = f"SELECT * FROM flights WHERE arrival_airport={arrival_airport}"
            else:
                query = f"SELECT * FROM flights WHERE arrival_airport={arrival_airport} AND origin_airport={origin_airport}"

            self.cursor.execute(query)
            flights = self.cursor.fetchall()
            if len(flights) == 0:
                return None
            else:
                flightList = []
                for flightRecord in flights:
                    iata_code = flightRecord[1]
                    origin_airport = flightRecord[2]
                    arrival_airport = flightRecord[3]
                    timestamp = flightRecord[4]

                    obj = Flight(iata_code, origin_airport, arrival_airport, timestamp)
                    flightList.append(obj)

                return flightList
        except Exception as e:
            print("Fout bij uitvoeren query: ", e)

    def add_flight(self, iata, origin, arrival, timestamp):
        try:
            self.cursor.execute("INSERT INTO flights (iata_code, origin_airport, arrival_airport, timestamp) VALUES (?, ?, ?, ?)", (iata, origin, arrival, timestamp))
            self.db_connectie.commit()
        except Exception as e:
            print("Fout bij uitvoeren query: ", e)

    def cancel_flight(self, iata_code):
        try:
            self.cursor.execute(f"DELETE FROM flights WHERE UPPER(iata_code) = '{iata_code.upper()}'")
            self.db_connectie.commit()
        except Exception as e:
            print("Fout bij uitvoeren query", e)