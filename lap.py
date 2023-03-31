import player as p

class Lap:

    def __init__(self, Id, Map, LapTime):
        self.Id = Id.int()
        self.Map = Map.str()
        self.LapTime = LapTime.DateTime()
        self.Player = p.Player()

    def __str__(self):
        return f"Id: {self.Id}, Map: {self.Map}, LapTime: {self.LapTime}, PlayerName: {self.Player}"