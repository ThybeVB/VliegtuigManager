import sqlite3, sys, os
from model.Flight import Flight

class DbManager:
    
    def __init__(self, db_file):
        try:
            self.db_connectie = sqlite3.connect(db_file)
            self.cursor = self.db_connectie.cursor()

            self.initialize()

        except:
            print("Geen connectie met database mogelijk")
            sys.exit(-1)

    def initialize(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS flights (id INTEGER PRIMARY KEY, iata_code TEXT, origin_airport TEXT, arrival_airport TEXT, timestamp TEXT)''')
        self.db_connectie.commit()

    # todo: uitbreiden met zoeken op datum, bestemming
    def get_flights(self):
        try:
            self.cursor.execute('''SELECT * FROM flights''')
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

