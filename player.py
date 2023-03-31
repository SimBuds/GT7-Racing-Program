class Player:
    def __init__(self, Id, Name, CarType, CarNumber):
        self.Id = Id.int()
        self.Name = Name.str()
        self.CarType = CarType.str()
        self.CarNumber = CarNumber.str()
        self.Laps = []

    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}, CarType: {self.CarType}, CarNumber: {self.CarNumber}"