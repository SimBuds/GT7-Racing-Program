import sqlite3 as sql
from sqlite3 import Error
import os as os

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
                                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                Name TEXT, 
                                CarType TEXT, 
                                CarNumber TEXT)""")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS Laps (
                                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Map TEXT,
                                LapTime TEXT,
                                PlayerId INTEGER,
                                FOREIGN KEY(PlayerId) REFERENCES Players(Id))""")
            self.connection.commit()
        else:
            print("Error: Connection failed")

    def LoadPlayers(self):
        self.cursor.execute("SELECT * FROM Players")
        players = self.cursor.fetchall()
        for player in players:
            self.players.append(Player(player[0], player[1], player[2], player[3]))

    def LoadLaps(self):
        self.cursor.execute("SELECT * FROM Laps")
        laps = self.cursor.fetchall()
        for lap in laps:
            self.laps.append(Lap(lap[0], lap[1], lap[2], lap[3]))

    def AddPlayer(self, name, carType, carNumber):
        self.cursor.execute("INSERT INTO Players (Name, CarType, CarNumber) VALUES (?, ?, ?)", (name, carType, carNumber))
        self.connection.commit()
        self.players.append(Player(self.cursor.lastrowid, name, carType, carNumber))

    def AddLap(self, map, lapTime, playerId):
        self.cursor.execute("INSERT INTO Laps (Map, LapTime, PlayerId) VALUES (?, ?, ?)", (map, lapTime, playerId))
        self.connection.commit()
        self.laps.append(Lap(self.cursor.lastrowid, map, lapTime, playerId))

    def GetPlayer(self, id):
        for player in self.players:
            if player.id == id:
                return player
        return None
    
    def GetLaps(self, playerId):
        laps = []
        for lap in self.laps:
            if lap.playerId == playerId:
                laps.append(lap)
        return laps
    
    def GetBestLap(self, playerId):
        bestLap = None
        for lap in self.laps:
            if lap.playerId == playerId:
                if bestLap == None:
                    bestLap = lap
                elif lap.lapTime < bestLap.lapTime:
                    bestLap = lap
        return bestLap
    
    def GetBestLapTime(self, playerId):
        bestLap = self.GetBestLap(playerId)
        if bestLap != None:
            return bestLap.lapTime
        return None
    
    def GetBestLapMap(self, playerId):
        bestLap = self.GetBestLap(playerId)
        if bestLap != None:
            return bestLap.map
        return None
    
    def GetAverageLapTime(self, playerId):
        laps = self.GetLaps(playerId)
        if len(laps) > 0:
            total = 0
            for lap in laps:
                total += lap.lapTime
            return total / len(laps)
        return None
    
    def GetAverageLapTimeByMap(self, playerId, map):
        laps = self.GetLaps(playerId)
        if len(laps) > 0:
            total = 0
            count = 0
            for lap in laps:
                if lap.map == map:
                    total += lap.lapTime
                    count += 1
            return total / count
        return None