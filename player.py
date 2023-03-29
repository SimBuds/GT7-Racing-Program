import lap as Lap

class Player:
    def __init__(self, Id, Name):
        self.Id = Id
        self.Name = Name
        self.Laps = []

    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}, Laps: {self.Laps}"

    