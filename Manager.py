import sqlite3 as sql
from sqlite3 import Error
import os as os

class Manager:
    
    def __init__(self):
        self.Connection = self.CreateConnection()
        self.Cursor = self.Connection.cursor()
        self.Maps = ["Bathurst Mt. panorama", "Monza", "Spa", "Nurburgring", "Suzuka", "Watkins Glen"]
        self.Players = []
        self.Laps = []
        if self.Connection is not None:
            self.CreateDB()
            self. LoadPlayers()
            self. LoadLaps()
        else:
            print("Error: Connection failed")

    def CreateConnection(self):
        try:
            Connection = sql.connect("Database.db")
            return Connection
        except Error as e:
            print(e)
        return None
    
    def CreateDB(self):
        if self.Connection is not None:
            self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Players (
                                Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                Name TEXT, 
                                CarType TEXT, 
                                CarNumber TEXT)""")
            self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Laps (
                                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Map TEXT,
                                LapTime TEXT,
                                PlayerId INTEGER,
                                FOREIGN KEY(PlayerId) REFERENCES Players(Id))""")
            self.Connection.commit()
        else:
            print("Error: Connection failed")

    def LoadPlayers(self):
        self.Cursor.execute("SELECT * FROM Players")
        Players = self.Cursor.fetchall()
        for Player in Players:
            self.Players.append(Player)

    def LoadLaps(self):
        self.Cursor.execute("SELECT * FROM Laps")
        Laps = self.Cursor.fetchall()
        for Lap in Laps:
            self.Laps.append(Lap)

    def AddPlayer(self, Name, CarType, CarNumber):
        self.Cursor.execute("INSERT INTO Players (Name, CarType, CarNumber) VALUES (?, ?, ?)", (Name, CarType, CarNumber))
        self.Connection.commit()
        self.Players.append((self.Cursor.lastrowid, Name, CarType, CarNumber))

    def AddLap(self, Map, LapTime, PlayerId):
        self.Cursor.execute("INSERT INTO Laps (Map, LapTime, PlayerId) VALUES (?, ?, ?)", (Map, LapTime, PlayerId))
        self.Connection.commit()
        self.Laps.append((self.Cursor.lastrowid, Map, LapTime, PlayerId))
    
    def RemovePlayer(self, Id):
        self.Cursor.execute("DELETE FROM Players WHERE Id = ?", (Id))
        self.Connection.commit()
        for Player in self.Players:
            if Player[0] == Id:
                self.Players.remove(Player)
                break

    def RemoveLap(self, Id, Map, LapTime):
        self.Cursor.execute("DELETE FROM Laps WHERE Id = ?", (Id))
        self.Connection.commit()
        for Lap in self.Laps:
            if Lap[0] == Id:
                self.Laps.remove(Lap)
                break

    def SearchLap(self, Map):
        for Lap in self.Laps:
            if Lap[1] == Map:
                print(Lap)
                
    def SearchPlayer(self, Name):
        for Player in self.Players:
            if Player[1] == Name:
                print(Player)

    def DisplayLap(self):
        for Lap in self.Laps:
            print(Lap)
    
    def DisplayLap(self, Id):
        for Lap in self.Laps:
            if Lap[0] == Id:
                print(Lap)

    def DisplayPlayer(self, Id):
        for Player in self.Players:
            if Player[0] == Id:
                print(Player)
