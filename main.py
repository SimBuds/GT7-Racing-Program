import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
from manager import Manager

manager = Manager()

class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Lap Time Tracker")
        self.master.resizable(False, False)
        self.pack()
        self.CenterWindow()
        self.Menu()

    def CenterWindow(self):
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = (screenWidth / 2) - (600 / 2)
        y = (screenHeight / 2) - (600 / 2)
        self.master.geometry(f"600x600+{int(x)}+{int(y)}")

    def Menu(self):
        self.menu = tk.Menu(self.master)
        self.master.resizable(False, False)
        self.CenterWindow()
        self.master.grab_set()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        
        self.lbl1 = tk.Label(self, text="Grand Turismo 7 Lap Time Tracker", font=("Helvetica", 16, "bold"))
        self.lbl1.grid(row=0, column=0, columnspan=2, pady=20, sticky='n')

        self.mapLabel = tk.Label(self, text="Choose a circuit to record your lap time:", font=("Helvetica", 12))
        self.mapLabel.grid(row=1, column=0, columnspan=2, pady=10, sticky='n')

        self.mapImages = []
        for map in manager.maps:
            mapImage = tk.PhotoImage(file=f"images/{map}.png")
            self.mapImages.append(mapImage)

        self.mapLabels = []
        for i in range(len(self.mapImages)):
            label = tk.Label(self, image=self.mapImages[i], borderwidth=2, relief="groove")
            tk.Label(self, text=manager.maps[i], font=("Helvetica", 12, "bold"))
            label.bind("<Button-1>", lambda event, index=i: self.OnMapClick(index))
            label.bind("<Enter>", lambda event, index=i: self.OnMapHover(index))
            label.grid(row=i // 2 + 2, column=i % 2, padx=20, pady=10, sticky='wens')
            self.mapLabels.append(label)

        self.showPlayersButton = tk.Button(self, text="Show Players", command=self.ViewAllPlayers)
        self.showPlayersButton.grid(row=5, column=0, pady=10, padx=(0, 10), sticky='e')

        self.addPlayerButton = tk.Button(self, text="Add Player", command=self.AddPlayer)
        self.addPlayerButton.grid(row=5, column=1, pady=10, padx=(10, 0), sticky='w')

        self.selectedMapLabel = tk.Label(self, text="No circuit Selected", font=("Helvetica", 12, "bold"))
        self.selectedMapLabel.grid(row=6, column=0, columnspan=2, pady=10, sticky='n')

        self.updateWindowSize()

    def updateWindowSize(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        self.master.geometry(f"{width}x{height}")

    def OnMapHover(self, index):
        mapName = manager.maps[index]
        self.selectedMapLabel.config(text=f"Map: {mapName}")

    def OnMapClick(self, index):
        self.selectedMapIndex = index
        self.selectedMapLabel.config(text=manager.maps[index])
        self.AddLap()

    def AddLap(self):
        self.addLapWindow = tk.Toplevel(self.master)
        self.addLapWindow.transient(self.master)
        self.addLapWindow.title("Add Lap")
        self.addLapWindow.resizable(False, False)
        self.addLapWindow.grab_set()

        self.addLapWindow.columnconfigure(0, weight=1)
        self.addLapWindow.columnconfigure(1, weight=1)
        self.addLapWindow.rowconfigure(0, weight=1)
        self.addLapWindow.rowconfigure(1, weight=1)

        self.addLapFrame = tk.Frame(self.addLapWindow)
        self.addLapFrame.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

        averageLap = manager.GetAverageLap(self.selectedMapLabel.cget("text"))
        self.averageLabel = tk.Label(self.addLapFrame, text=f"Average Lap Time: {averageLap if averageLap is not None else 'N/A'}", font=("Helvetica", 12, "bold"))
        self.averageLabel.grid(row=0, column=0, columnspan=2, pady=20)

        bestLap = manager.GetBestLap(self.selectedMapLabel.cget("text"))
        self.bestLabel = tk.Label(self.addLapFrame, text=f"Best Lap Time: {bestLap if bestLap is not None else 'N/A'}", font=("Helvetica", 12, "bold"))
        self.bestLabel.grid(row=1, column=0, columnspan=2, pady=20)

        self.carLabel = tk.Label(self.addLapFrame, text="Car:", font=("Helvetica", 10))
        self.carLabel.grid(row=2, column=0, pady=20)

        self.carEntry = tk.Entry(self.addLapFrame)
        self.carEntry.grid(row=2, column=1, pady=20)

        self.timeLabel = tk.Label(self.addLapFrame, text="Lap Time:", font=("Helvetica", 10))
        self.timeLabel.grid(row=3, column=0, pady=20)

        self.timeEntry = tk.Entry(self.addLapFrame)
        self.timeEntry.grid(row=3, column=1, pady=20)

        self.playerLabel = tk.Label(self.addLapFrame, text="Player:", font=("Helvetica", 10))
        self.playerLabel.grid(row=4, column=0, pady=20)

        self.selected_player = tk.StringVar(self.addLapFrame)
        self.selected_player.set("Select a player")
        players = manager.GetAllPlayers()
        self.playerMenu = tk.OptionMenu(self.addLapFrame, self.selected_player, *players)
        self.playerMenu.grid(row=4, column=1, pady=20)

        self.addLapButton = tk.Button(self.addLapFrame, text="Add Lap", command=self.AddLapToDB)
        self.addLapButton.grid(row=5, column=0, columnspan=2, pady=20)

        self.showAllLapsButton = tk.Button(self.addLapFrame, text="Show All Laps", command=self.ViewAllLaps)
        self.showAllLapsButton.grid(row=6, column=0, columnspan=2, pady=20)

        self.addLapWindow.update()
        self.addLapWindow.minsize(self.addLapWindow.winfo_width(), self.addLapWindow.winfo_height())
        self.addLapWindow.geometry(f"+{int((self.addLapWindow.winfo_screenwidth() / 2) - (self.addLapWindow.winfo_width() / 2))}+{int((self.addLapWindow.winfo_screenheight() / 2) - (self.addLapWindow.winfo_height() / 2))}")

    def AddLapToDB(self):
        mapName = self.selectedMapLabel.cget("text")
        carType = self.carEntry.get()
        lapTime = self.timeEntry.get()
        playerName = self.selected_player.get()

        if carType and lapTime and playerName != "Select a player":
            try:
                lapTimeTest = float(lapTime)
                if lapTimeTest <= 0:
                    raise ValueError("Lap time must be greater than 0.")
            except ValueError as e:
                messagebox.showerror("Error", f"Invalid lap time: {e}")
                return
            added = manager.AddLap(mapName, carType, lapTime, playerName)
            if added:
                messagebox.showinfo("Success", "Lap added successfully.")
                self.addLapWindow.destroy()
            else:
                messagebox.showerror("Error", "Failed to add lap.")
        else:
            messagebox.showerror("Error", "All fields must be filled.")

    def ViewAllLaps(self):
        self.viewLapsWindow = tk.Toplevel(self.master)
        self.viewLapsWindow.title("Laps")
        self.viewLapsWindow.transient(self.master)
        self.viewLapsWindow.grab_set()
        self.viewLapsWindow.resizable(False, False)

        self.viewLapsFrame = tk.Frame(self.viewLapsWindow)
        self.viewLapsFrame.grid(padx=20, pady=20)

        self.scrollbar = ttk.Scrollbar(self.viewLapsFrame)
        self.scrollbar.grid(row=0, column=1, sticky="ns", padx=10)

        self.lapsListbox = tk.Listbox(self.viewLapsFrame, width=80, height=20, font=("Helvetica", 12), yscrollcommand=self.scrollbar.set, justify=tk.CENTER)
        self.lapsListbox.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.config(command=self.lapsListbox.yview)

        self.lapsListbox.bind("<<ListboxSelect>>", self.OnLapSelect)

        laps = manager.GetAllLaps(self.selectedMapLabel.cget("text"))

        for lap in laps:
            self.lapsListbox.insert(tk.END, lap)

        self.selectedLapLabel = tk.Label(self.viewLapsFrame, text="Selected Lap: N/A", font=("Helvetica", 12, "bold"))
        self.selectedLapLabel.grid(row=1, column=0, columnspan=2, pady=20)

        self.viewLapsWindow.update()
        self.viewLapsWindow.minsize(self.viewLapsWindow.winfo_width(), self.viewLapsWindow.winfo_height())
        self.viewLapsWindow.geometry(f"+{int((self.viewLapsWindow.winfo_screenwidth() / 2) - (self.viewLapsWindow.winfo_width() / 2))}+{int((self.viewLapsWindow.winfo_screenheight() / 2) - (self.viewLapsWindow.winfo_height() / 2))}")


    def OnLapSelect(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            value = widget.get(index)
            self.selectedLapLabel.config(text=value)

    def ViewAllPlayers(self):
        self.viewPlayersWindow = tk.Toplevel(self.master)
        self.viewPlayersWindow.title("Players")
        self.viewPlayersWindow.transient(self.master)
        self.viewPlayersWindow.resizable(False, False)
        self.viewPlayersWindow.grab_set()

        self.viewPlayersFrame = tk.Frame(self.viewPlayersWindow)
        self.viewPlayersFrame.grid(padx=20, pady=20)

        self.scrollbar = ttk.Scrollbar(self.viewPlayersFrame)
        self.scrollbar.grid(row=0, column=1, sticky="ns", padx=10)

        self.playersListbox = tk.Listbox(self.viewPlayersFrame, width=30, height=15, font=("Helvetica", 12), yscrollcommand=self.scrollbar.set, justify=tk.CENTER)
        self.playersListbox.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.config(command=self.playersListbox.yview)

        players = manager.GetAllPlayers()

        for player in players:
            self.playersListbox.insert(tk.END, player.name)

        self.editPlayerButton = tk.Button(self.viewPlayersFrame, text="Update Player", command=self.EditPlayer)
        self.editPlayerButton.grid(row=1, column=0, pady=10)

        self.deletePlayerButton = tk.Button(self.viewPlayersFrame, text="Delete Player", command=self.DeletePlayer)
        self.deletePlayerButton.grid(row=2, column=0, pady=10)

        self.viewPlayersWindow.update()
        self.viewPlayersWindow.minsize(self.viewPlayersWindow.winfo_width(), self.viewPlayersWindow.winfo_height())
        self.viewPlayersWindow.geometry(f"+{int((self.viewPlayersWindow.winfo_screenwidth() / 2) - (self.viewPlayersWindow.winfo_width() / 2))}+{int((self.viewPlayersWindow.winfo_screenheight() / 2) - (self.viewPlayersWindow.winfo_height() / 2))}")

    def DeletePlayer(self):
        selected = self.playersListbox.curselection()
        if selected:
            selected = self.playersListbox.get(selected)
            deleted = manager.DeletePlayer(selected)
            if deleted:
                messagebox.showinfo("Success", "Player deleted successfully.")
                self.viewPlayersWindow.destroy()
            else:
                messagebox.showerror("Error", "Failed to delete player.")
        else:
            messagebox.showerror("Error", "No player selected.")

    def EditPlayer(self):
        self.editPlayerWindow = tk.Toplevel(self.master)
        self.editPlayerWindow.transient(self.master)
        self.editPlayerWindow.title("Edit Player")
        self.editPlayerWindow.resizable(False, False)
        self.editPlayerWindow.grab_set()

        self.editPlayerLabel = tk.Label(self.editPlayerWindow, text="Enter New Player Name:")
        self.editPlayerLabel.grid(row=0, column=0, padx=20, pady=10, sticky='e')

        self.playerNameEntry = tk.Entry(self.editPlayerWindow)
        self.playerNameEntry.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        self.updatePlayerButton = tk.Button(self.editPlayerWindow, text="Update Player", command=self.UpdatePlayerInDB)
        self.updatePlayerButton.grid(row=1, column=0, columnspan=2, pady=10)

        self.editPlayerWindow.update()
        self.editPlayerWindow.minsize(self.editPlayerWindow.winfo_width(), self.editPlayerWindow.winfo_height())
        self.editPlayerWindow.geometry(f"+{int((self.editPlayerWindow.winfo_screenwidth() / 2) - (self.editPlayerWindow.winfo_width() / 2))}+{int((self.editPlayerWindow.winfo_screenheight() / 2) - (self.editPlayerWindow.winfo_height() / 2))}")

    def UpdatePlayerInDB(self):
        playerName = self.playerNameEntry.get()
        if playerName != "":
            selected = self.playersListbox.curselection()
            if selected:
                oldName = self.playersListbox.get(selected)
                updated = manager.EditPlayer(oldName, playerName)
                if updated:
                    messagebox.showinfo("Success", "Player updated successfully.")
                    self.editPlayerWindow.destroy()
                    self.viewPlayersWindow.destroy()
                    self.ViewAllPlayers()
                else:
                    messagebox.showerror("Error", "Failed to update player.")
            else:
                messagebox.showerror("Error", "No player selected.")
        else:
            messagebox.showerror("Error", "Player name cannot be empty.")

    def AddPlayer(self):
        self.addPlayerWindow = tk.Toplevel(self.master)
        self.addPlayerWindow.transient(self.master)
        self.addPlayerWindow.title("Add Player")
        self.addPlayerWindow.resizable(False, False)
        self.addPlayerWindow.grab_set()
        self.addPlayerLabel = tk.Label(self.addPlayerWindow, text="Enter Player Name:")
        self.addPlayerLabel.grid(row=0, column=0, padx=20, pady=10, sticky='e')

        self.playerNameEntry = tk.Entry(self.addPlayerWindow)
        self.playerNameEntry.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        self.submitPlayerButton = tk.Button(self.addPlayerWindow, text="Add Player", command=self.AddPlayerToDB)
        self.submitPlayerButton.grid(row=1, column=0, columnspan=2, pady=10)

        self.addPlayerWindow.update()
        self.addPlayerWindow.minsize(self.addPlayerWindow.winfo_width(), self.addPlayerWindow.winfo_height())
        self.addPlayerWindow.geometry(f"+{int((self.addPlayerWindow.winfo_screenwidth() / 2) - (self.addPlayerWindow.winfo_width() / 2))}+{int((self.addPlayerWindow.winfo_screenheight() / 2) - (self.addPlayerWindow.winfo_height() / 2))}")

    def AddPlayerToDB(self):
        playerName = self.playerNameEntry.get().strip()
        if playerName != "":
            added = manager.AddPlayer(playerName)
            if added:
                messagebox.showinfo("Success", "Player added successfully.")
                self.addPlayerWindow.destroy()
            else:
                messagebox.showerror("Error", "Failed to add player.")
        else:
            messagebox.showerror("Error", "Player name cannot be empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()