class Lap:
    def __init__(self, id, map, carType, lapTime, playerId):
        self.id = id
        self.map = map
        self.carType = carType
        self.lapTime = lapTime
        self.playerId = playerId

    def __str__(self):
        return f"Id: {self.id}, Map: {self.map}, Car Type: {self.carType}, Lap Time: {self.lapTime}, Player Id: {self.playerId}"