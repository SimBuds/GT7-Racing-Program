import player as p

class Lap:

    def __init__(self, id, map, lapTime):
        self.Id = id.int()
        self.Map = map.toTitle()
        self.LapTime = lapTime.float()
        self.Player = p.Player

    def __str__(self):
        return f"Id: {self.id}, Map: {self.map}, LapTime: {self.lapTime}, Player: {self.player}"