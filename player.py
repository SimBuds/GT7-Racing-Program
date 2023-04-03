class Player:

    def __init__(self, playerId, name):
        self.id = playerId
        self.name = name

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}"