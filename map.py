import lap as Lap

class Map:
    
    def __init__(self, Id, MapName):
        self.Id = Id.int()
        self.MapName = MapName.str()
        self.Laps = []

    def __str__(self):
        return f"Id: {self.Id}, MapName: {self.MapName}, Laps: {self.Laps}"