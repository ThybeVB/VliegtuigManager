from database.DbManager import DbManager

class DbPlane(DbManager):

    def __init__(self, db_file):
        super().__init__(db_file)


    def add_plane(self, registration, type, airline):
        pass

    def remove_plane(self, registration):
        pass

    def modify_plane(self, registration, type, airline):
        pass