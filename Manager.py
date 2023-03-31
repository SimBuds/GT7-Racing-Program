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