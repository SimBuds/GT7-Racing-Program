import sqlite3 as sql
from sqlite3 import Error
import os as os
import lap as Lap
import player as Player

class Manager:
    
    def __init__(self):
        self.connection = self.CreateConnection()
        self.cursor = self.connection.cursor()
        self.maps = ["Bathurst Mt. panorama", "Monza", "Spa", "Nurburgring", "Suzuka", "Watkins Glen"]
        self.players = []
        self.laps = []
        if self.connection is not None:
            self.CreateDB()
            self. LoadPlayers()
            self. LoadLaps()
        else:
            print("Error: Connection failed")

    def CreateConnection(self):
        try:
            connection = sql.connect("RacingManager.db")
            return connection
        except Error as e:
            print(e)
        return None
    
    def CreateDB(self):
        if self.connection is not None:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Players (
                                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                name TEXT)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Laps (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                map TEXT,
                                carType TEXT,
                                lapTime REAL,
                                playerId INTEGER NOT NULL REFERENCES Players(id))""")
    def LoadPlayers(self):
        self.cursor.execute("SELECT * FROM Players")
        players = self.cursor.fetchall()
        for player in players:
            self.players.append(Player(player[0], player[1]))
    
    def LoadLaps(self):
        self.cursor.execute("SELECT * FROM Laps")
        laps = self.cursor.fetchall()
        for lap in laps:
            self.laps.append(Lap(lap[0], lap[1], lap[2], lap[3], lap[4]))

    #Add lap to database while creating a user if they don't exist
    def AddPlayer(self, name):
        player = self.GetPlayer(name)
        if player is None:
            self.cursor.execute("INSERT INTO Players (name) VALUES (?)", (name,))
            self.connection.commit()
            player_id = self.cursor.lastrowid
            new_player = Player(player_id, name)
            self.players.append(new_player)
            return new_player
        else:
            return player

    def GetPlayer(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def AddLap(self, map, carType, lapTime, playerName):
        player = self.AddPlayer(playerName)
        self.cursor.execute("INSERT INTO Laps (map, carType, lapTime, playerId) VALUES (?, ?, ?, ?)", (map, carType, lapTime, player.id))
        self.connection.commit()
        lap_id = self.cursor.lastrowid
        new_lap = Lap(lap_id, map, carType, lapTime, player.id)
        self.laps.append(new_lap)
        return new_lap

    #View laps for a specific map
    def ViewLaps(self, map):
        for lap in self.laps:
            if lap.map == map:
                print(lap)

    