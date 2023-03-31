from Manager import Manager
import tkinter
from tkinter import *
from tkinter import ttk
import application as app
manager = Manager()
manager.CreateDB()

def openNewCircuit():
    newCircuitWindow = Tk()
    newCircuitWindow.title("Add a New Circuit")
    newCircuitWindow.geometry("300x300")
    frm = ttk.Frame(newCircuitWindow, padding=10)
    frm.grid()
    ttk.Label(frm, text="Circuit Name").grid(column=0, row=0)
    nameBox = ttk.Entry(newCircuitWindow).grid(column=0,row=1)
    ttk.Button(frm, text="Submit", command=manager.AddMap("ZOLDER")).grid(column=0, row=2)

def openNewPlayer():
    newPlayerWindow = Tk()
    newPlayerWindow.title("Add a New Player")
    newPlayerWindow.geometry("300x300")

def openNewLap():
    newLapWindow = Toplevel()
    newLapWindow.title("Add a New Fastest Lap")
    newLapWindow.geometry("300x300")

def openViewCircuits():
    viewCircuitWindow = Toplevel()
    viewCircuitWindow.title("Players")
    viewCircuitWindow.geometry("300x300")

def openViewPlayers():
    viewPlayerWindow = Toplevel()
    viewPlayerWindow.title("Players")
    viewPlayerWindow.geometry("300x300")

def openLeaderboards():
    leaderboardWindow = Toplevel()
    leaderboardWindow.title("Leaderboard")
    leaderboardWindow.geometry("300x300")




root = Tk()
root.geometry("300x300")
root.title("Gran Turismo Tracker")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Weclome to the GT7 Lap Tracker!").grid(column=0, row=0)
ttk.Button(frm, text="Add a Circuit", command=openNewCircuit).grid(column=0, row=1)
ttk.Button(frm, text="Add a Player", command=openNewPlayer).grid(column=0, row=2)
ttk.Button(frm, text="Enter a new Lap", command=openNewLap).grid(column=0, row=3)
ttk.Button(frm, text="Circuits", command=openViewCircuits).grid(column=0, row=4)
ttk.Button(frm, text="Players", command=openViewPlayers).grid(column=0, row=5)
ttk.Button(frm, text="Fastest Laps", command=openLeaderboards).grid(column=0, row=6)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=0, row=7)
root.mainloop()

#
# app.run()