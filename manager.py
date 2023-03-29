import sqlite3 as sql
from sqlite3 import Error
import os as os

class Manager:
    
    def __init__(self):
        self. Connection = self.CreateConnection()
        self. Cursor = self.Connection.cursor()
        self. Maps = []
        self. Players = []
        self. Laps = []
        if self.Connection is not None:
            self.CreateDB()
            self. LoadMaps()
            self. LoadPlayers()
            self. LoadLaps()
        else:
            print("Error: Connection failed")

    def CreateConnection(self):
        try:
            if not os.path.exists(os.path.dirname(os.path.abspath(__file__)) + "/database.db"):
                open(os.path.dirname(os.path.abspath(__file__)) + "/database.db", "w+")
            Connection = sql.connect(os.path.dirname(os.path.abspath(__file__)) + "/database.db")
            return Connection
        except Error as e:
            print(e)
        return None
    
    def CreateDB(self):
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Map(
            Id INTEGER PRIMARY KEY,
            MapName TEXT)""")
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Player(
            Id INTEGER PRIMARY KEY,
            Name TEXT)""")
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS Laps(
            Id INTEGER PRIMARY KEY,
            MapId INTEGER,
            LapTime INTEGER,
            PlayerId INTEGER,
            FOREIGN KEY (MapId) REFERENCES Map(Id),
            FOREIGN KEY (PlayerId) REFERENCES Player(Id))""")
        self.Connection.commit()

    def LoadMaps(self):
        self.Cursor.execute("SELECT * FROM Map")
        self.Maps = self.Cursor.fetchall()

    def LoadPlayers(self):
        self.Cursor.execute("SELECT * FROM Player")
        self.Players = self.Cursor.fetchall()

    def LoadLaps(self):
        self.Cursor.execute("SELECT * FROM Laps")
        self.Laps = self.Cursor.fetchall()

    def AddMap(self, MapName):
        try:
            self.Cursor.execute("INSERT INTO Map (MapName) VALUES (?)", (MapName,))
            self.Connection.commit()
            self.LoadMaps()
        except Error as e:
            print(e)

    def AddPlayer(self, PlayerName):
        try:
            self.Cursor.execute("INSERT INTO Player (Name) VALUES (?)", (PlayerName,))
            self.Connection.commit()
            self.LoadPlayers()
        except Error as e:
            print(e)

    def AddLap(self, MapId, LapTime, PlayerId):
        try:
            self.Cursor.execute("INSERT INTO Laps (MapId, LapTime, PlayerId) VALUES (?, ?, ?)", (MapId, LapTime, PlayerId))
            self.Connection.commit()
            self.LoadLaps()
        except Error as e:
            print(e)

    def DisplayMaps(self):
        for Map in self.Maps:
            print(Map)

    def DisplayPlayers(self):
        for Player in self.Players:
            print(Player)

    def DisplayLaps(self):
        for Lap in self.Laps:
            print(Lap)    