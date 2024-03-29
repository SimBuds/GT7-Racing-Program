class Player:

    def __init__(self, playerId, name):
        self.id = playerId
        self.name = name

    def __str__(self):
        return f"{self.name}"
class Lap:
    
    def __init__(self, id, map, carType, lapTime, playerId):
        self.id = id
        self.map = map
        self.carType = carType
        self.lapTime = float(lapTime)
        self.playerId = playerId

    def __str__(self):
        return f" Map: {self.map}, Car Type: {self.carType}, Lap Time: {self.lapTime}, Player Id: {self.playerId}"