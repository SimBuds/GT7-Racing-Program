import sqlite3 as sql
from sqlite3 import Error
import os as os
import player as Player
import lap as Lap

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
            self.connection.commit()
        else:
            print("Error: Connection failed")

    def LoadPlayers(self):
        self.cursor.execute("SELECT * FROM Players")
        players = self.cursor.fetchall()
        for player in players:
            self.players.append(Player.Player(player[0], player[1]))
    
    def LoadLaps(self):
        self.cursor.execute("SELECT * FROM Laps")
        laps = self.cursor.fetchall()
        for lap in laps:
            self.laps.append(Lap.Lap(lap[0], lap[1], lap[2], lap[3], lap[4]))

    #Add lap to database while creating a user if they don't exist
    def AddPlayer(self, name):
        player = self.GetPlayer(name)
        if player is None:
            self.cursor.execute("INSERT INTO Players (name) VALUES (?)", (name,))
            self.connection.commit()
            playerId = self.cursor.lastrowid
            newPlayer = Player(playerId, name)
            self.players.append(newPlayer) 
            return newPlayer
        else:
            return player


    def GetPlayer(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None

    def AddLap(self, map, carType, lapTime, playerName):
        player = self.AddPlayer(playerName)
        if player is not None:
            self.cursor.execute("INSERT INTO Laps (map, carType, lapTime, playerId) VALUES (?, ?, ?, ?)", (map, carType, lapTime, player.id))
            self.connection.commit()
            lapId = self.cursor.lastrowid
            newLap = Lap(lapId, map, carType, lapTime, player.id)
            self.laps.append(newLap)
            return newLap
        else:
            return None

    #View laps for a specific map
    def ViewLaps(self, map):
        for lap in self.laps:
            if lap.map == map:
                print(lap)

    