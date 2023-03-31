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

    # SQL Functions
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

    def EditLap(self, Id, MapId, LapTime, PlayerId):
        try:
            self.Cursor.execute("UPDATE Laps SET MapId = ?, LapTime = ?, PlayerId = ? WHERE Id = ?", (MapId, LapTime, PlayerId, Id))
            self.Connection.commit()
            self.LoadLaps()
        except Error as e:
            print(e)

    def EditMap(self, Id, MapName):
        try:
            self.Cursor.execute("UPDATE Map SET MapName = ? WHERE Id = ?", (MapName, Id))
            self.Connection.commit()
            self.LoadMaps()
        except Error as e:
            print(e)


    def EditPlayer(self, Id, PlayerName):
        try:
            self.Cursor.execute("UPDATE Player SET Name = ? WHERE Id = ?", (PlayerName, Id))
            self.Connection.commit()
            self.LoadPlayers()
        except Error as e:
            print(e)
    
    def DeleteLap(self, Id):
        try:
            self.Cursor.execute("DELETE FROM Laps WHERE Id = ?", (Id,))
            self.Connection.commit()
            self.LoadLaps()
        except Error as e:
            print(e)

    def DeleteMap(self, Id):
        try:
            self.Cursor.execute("DELETE FROM Map WHERE Id = ?", (Id,))
            self.Connection.commit()
            self.LoadMaps()
        except Error as e:
            print(e)

    def DeletePlayer(self, Id):
        try:
            self.Cursor.execute("DELETE FROM Player WHERE Id = ?", (Id,))
            self.Connection.commit()
            self.LoadPlayers()
        except Error as e:
            print(e)

    # Array Handling Functions
    def DisplayMaps(self):
        for Map in self.Maps:
            print(Map)

    def DisplayPlayers(self):
        for Player in self.Players:
            print(Player)

    def DisplayLaps(self):
        for Lap in self.Laps:
            print(Lap)

    def GetMap(self, Id):
        for Map in self.Maps:
            if Map[0] == Id:
                return Map
        return None
    
    def GetPlayer(self, Id):
        for Player in self.Players:
            if Player[0] == Id:
                return Player
        return None
    
    def GetLap(self, Id):
        for Lap in self.Laps:
            if Lap[0] == Id:
                return Lap
        return None
    
    def ShowAllMaps(self):
        for Map in self.Maps:
            print(Map[1])