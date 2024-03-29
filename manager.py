import sqlite3 as sql
from sqlite3 import Error
import os as os
from models import Player, Lap
import tkinter as tk
from tkinter import messagebox

class Manager:
    
    def __init__(self):
        self.connection = self.CreateConnection()
        self.cursor = self.connection.cursor()
        self.maps = ["Bathurst Mt. Panorama", "Monza", "Spa", "Nurburgring", "Suzuka", "Watkins Glen"]
        self.players = []
        self.laps = []
        if self.connection is not None:
            self.CreateDB()
            self.LoadPlayers()
            self.LoadLaps()
        else:
            print("Error: Connection failed")

    def CreateConnection(self):
        try:
            connection = sql.connect("database.db")
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
    
    def LapInputCheck(self, input):
        try:
            float(input)
        except ValueError:
            messagebox.showerror("Error", "Please input a lap time in format '<seconds>.<milliseconds>'")
            return False
        return True
    
    def CarInputCheck(self, input):
        if not  all(letter.isalnum() or letter.isspace() or letter == "-" or letter == "/" for letter in input):
            messagebox.showerror("Error", "The car name cannot contain a special character.")
            return False
        return True
    
    def PlayerInputCheck(self, input):
        if all(letter.isalpha() or letter.isspace() for letter in input):
            return True
        messagebox.showerror("Error", "The player name cannot contain special characters or numbers.")
        return False

    def AddPlayer(self, name):
        if not name.strip() or not self.PlayerInputCheck(name) or name == "":
            return False
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
        
    def DeletePlayer(self, name):
        player = self.GetPlayer(name)
        if player is not None:
            self.cursor.execute("DELETE FROM Players WHERE name = ?", (name,))
            self.cursor.execute("DELETE FROM Laps WHERE playerId = ?", (player.id,))
            self.connection.commit()
            self.players.remove(player)
            return True
        else:
            return False

    def EditPlayer(self, name, newName):
        if not newName.strip() or not self.PlayerInputCheck(newName):
            return False
        player = self.GetPlayer(name)
        if player is not None:
            self.cursor.execute("UPDATE Players SET name = ? WHERE name = ?", (newName, name))
            self.connection.commit()
            player.name = newName
            return True
        else:
            return False
        
    def GetPlayer(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def GetPlayerName(self, playerId):
        for player in self.players:
            if player.id == playerId:
                return f"{player.name}"
        return None
    
    def GetAllPlayers(self):
        return self.players
    
    def LoadLaps(self):
        self.cursor.execute("SELECT * FROM Laps")
        laps = self.cursor.fetchall()
        for lap in laps:
            self.laps.append(Lap(lap[0], lap[1], lap[2], lap[3], lap[4]))
    
    def GetLap(self, lapId):
        for lap in self.laps:
            if lap.id == lapId:
                return lap
        return None

    def AddLap(self, map, carType, lapTime, playerName):
        if lapTime == "" or not playerName.strip() or not self.LapInputCheck(lapTime) or carType == "" or not self.CarInputCheck(carType):
            return False

        playerId = self.AddPlayer(playerName)
        self.cursor.execute("INSERT INTO Laps (map, carType, lapTime, playerId) VALUES (?, ?, ?, ?)", (map, carType, lapTime, playerId))
        self.connection.commit()
        if playerId is not None:
            lapId = self.cursor.lastrowid
        lap = Lap(lapId, map, carType, lapTime, playerId)
        self.laps.append(lap)
        return True

    def GetBestLap(self, map):
        bestLap = None
        for lap in self.laps:
            if lap.map == map:
                if bestLap is None:
                    bestLap = lap
                elif lap.lapTime < bestLap.lapTime:
                    bestLap = lap
        if bestLap is not None:
            return f"{self.GetPlayerName(bestLap.playerId)}: {bestLap.lapTime}"
        else:
            return None

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

    def GetAllLaps(self, map):
        laps = []
        for lap in self.laps:
            if lap.map == map:
                laps.append(lap)
        return laps