class Lap:

    def __init__(self, Id, Map, LapTime, PlayerName):
        self.Id = Id.int()
        self.Map = Map.str()
        self.LapTime = LapTime.DateTime()
        self.PlayerName = PlayerName.str()

    def __str__(self):
        return f"Id: {self.Id}, Map: {self.Map}, LapTime: {self.LapTime}, PlayerName: {self.PlayerName}"