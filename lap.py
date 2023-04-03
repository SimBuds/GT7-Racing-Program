import player as p

class Lap:

    def __init__(self, id, map, lapTime):
        self.Id = id
        self.Map = map
        self.LapTime = lapTime
        self.Player = p.Player

    def __str__(self):
        return f"Id: {self.id}, Map: {self.map}, LapTime: {self.lapTime}, Player: {self.player}"