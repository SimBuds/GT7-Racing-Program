import player as p

class Lap:

    def __init__(self, id, map, carType, lapTime):
        self.id = id.int()
        self.map = map.toTitle()
        self.carType = carType.toTitle()
        self.lapTime = lapTime.float()
        self.player = p.Player

    def __str__(self):
        return f"Id: {self.id}, Map: {self.map}, Car Type: {self.carType}, Lap Time: {self.lapTime}, Player: {self.player}"