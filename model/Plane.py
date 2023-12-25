class Plane:
    
    def __init__(self, registration, type, airline):
        self.registration = registration
        self.type = type
        self.airline = airline

    def get_summary(self):
        return f"Vliegtuig {self.registration} van {self.airline} van het type {self.type}."