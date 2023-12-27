import sys, sqlite3

class DbManager:
    def __init__(self, db_file):
        try:
            self.db_connectie = sqlite3.connect(db_file)
            self.cursor = self.db_connectie.cursor()

            self.initialize()

        except Exception as e:
            print("Geen connectie met database mogelijk: ", e)
            sys.exit(-1)

    def initialize(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS flights(
                                id INTEGER PRIMARY KEY,
                                iata_code TEXT, 
                                origin_airport TEXT, 
                                arrival_airport TEXT, 
                                timestamp TEXT,
                                plane_registration TEXT, 
                                FOREIGN KEY (plane_registration) REFERENCES planes(registration))
                            ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS planes (registration TEXT PRIMARY KEY, type TEXT, airline TEXT)''')
        
        self.db_connectie.commit()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.db_connectie:
            self.db_connectie.close()
