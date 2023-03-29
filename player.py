import lap as Lap

class Player:
    def __init__(self, Id, Name):
        self.Id = Id.int()
        self.Name = Name.str()
        self.Laps = []

    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}, Laps: {self.Laps}"

    