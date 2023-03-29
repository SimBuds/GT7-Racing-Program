class Lap:

    def __init__(self, Id, Map, LapTime, PlayerName):
        self.Id = Id
        self.Map = Map
        self.LapTime = LapTime
        self.PlayerName = PlayerName

    def __str__(self):
        return f"Id: {self.Id}, Map: {self.Map}, LapTime: {self.LapTime}, PlayerName: {self.PlayerName}"