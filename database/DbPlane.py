from database.DbManager import DbManager
from model.Plane import Plane

class DbPlane(DbManager):

    def __init__(self, db_file):
        super().__init__(db_file)

    def get_planes(self):
        try:
            self.cursor.execute('''SELECT * FROM planes''')
            planes = self.cursor.fetchall()
            if len(planes) == 0:
                return None
            else:
                planeList = []
                for planeRecord in planes:
                    registration = planeRecord[0]
                    type = planeRecord[1]
                    airline = planeRecord[2]

                    obj = Plane(registration, type, airline)
                    planeList.append(obj)

                return planeList
        except Exception as e:
            print("Fout bij uitvoeren query: ", e)


    def get_plane(self, registration):
        try: 
            self.cursor.execute(f"SELECT * FROM planes WHERE UPPER(registration) = ?", (registration.upper(),))
            plane = self.cursor.fetchone()
            if plane is None:
                return None
            else:
                registration = plane[0]
                type = plane[1]
                airline = plane[2]

                obj = Plane(registration, type, airline)
                return obj            
        except Exception as e:
            print("Fout bij uitvoeren query", e)

    def add_plane(self, registration, type, airline):
        try:
            self.cursor.execute(f"INSERT INTO planes (registration, type, airline) VALUES (?, ?, ?)", (registration, type, airline))
            self.db_connectie.commit()
        except Exception as e:
            print("Fout bij uitvoeren query", e)

    def remove_plane(self, registration):
        try:
            self.cursor.execute(f"DELETE FROM planes WHERE UPPER(registration) = ?", (registration.upper(),))
            self.db_connectie.commit()
        except Exception as e:
            print("Fout bij uitvoeren query: ", e)

    def modify_plane(self, registration, type, airline):
        try:
            self.cursor.execute(f"UPDATE planes SET type = ?, airline = ? WHERE UPPER(registration) = ?", (type, airline, registration.upper()))
            self.db_connectie.commit()
        except Exception as e:
            print("Fout bij uitvoeren query: ", e)