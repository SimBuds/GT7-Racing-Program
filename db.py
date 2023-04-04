import sqlite3 as sql
from sqlite3 import Error
import os as os
from models import Player, Lap

class Manager:
    
    def __init__(self):
        self.connection = self.CreateConnection()
        self.cursor = self.connection.cursor()
        self.maps = ["Bathurst Mt. Panorama", "Monza", "Spa", "Nurburgring", "Suzuka", "Watkins Glen"]
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
            playerId = self.cursor.lastrowid
            player = Player(playerId, name)
            self.players.append(player)
            return player.id
        else:
            return player.id

    def GetPlayer(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def GetLap(self, lapId):
        for lap in self.laps:
            if lap.id == lapId:
                return lap
        return None

    def AddLap(self, map, carType, lapTime, playerName):
        playerId = self.AddPlayer(playerName)
        self.cursor.execute("INSERT INTO Laps (map, carType, lapTime, playerId) VALUES (?, ?, ?, ?)", (map, carType, float(lapTime), playerId))
        self.connection.commit()
        if playerId is not None:
            lapId = self.cursor.lastrowid
        lap = Lap(lapId, map, carType, lapTime, playerId)
        self.laps.append(lap)
        return True

    #View laps for a specific map
    def ViewLaps(self, map):
        for lap in self.laps:
            if lap.map == map:
                print(lap)

    #View all laps
    def ViewAllLaps(self):
        for lap in self.laps:
            print(lap)
    
    #View all players
    def ViewAllPlayers(self):
        for player in self.players:
            print(player)
    
    #View all laps for a specific player
    def ViewPlayerLaps(self, playerName):
        player = self.GetPlayer(playerName)
        if player is not None:
            for lap in self.laps:
                if lap.playerId == player.id:
                    print(lap)
        else:
            print("Player not found")

    # View best lap for a specific map
    def GetBestLap(self, map):
        bestLap = None
        for lap in self.laps:
            if lap.map == map:
                if bestLap is None:
                    bestLap = lap
                elif lap.lapTime < bestLap.lapTime:
                    bestLap = lap
        if bestLap is not None:
            return f"{bestLap.lapTime}"
        else:
            return None

    # View average lap time for a specific map
    def GetAverageLap(self, map):
        lapCount = 0
        lapTime = 0
        for lap in self.laps:
            if lap.map == map:
                lapCount += 1
                lapTime += float(lap.lapTime)
        if lapCount > 0:
            return f"{lapTime / lapCount:.2f}"
        else:
            return None