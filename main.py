import tkinter as tk
from tkinter import ttk
from db import Manager

manager = Manager()

class Main(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Lap Time Tracker")
        self.master.geometry("405x420")
        self.master.resizable(False, False)
        self.grid()

        self.lbl1 = tk.Label(self, text="Grand Turismo 7 Lap Time Tracker")
        self.lbl1.grid(row=0, column=0, columnspan=10, pady=10)
        
        self.mapLabel = tk.Label(self, text="Choose a map to record your lap time:")
        self.mapLabel.grid(row=1, column=0, columnspan=10, pady=10)

        # Create PhotoImage objects for the maps
        self.mapImages = []
        self.mapImages.append(tk.PhotoImage(file="maps/bathurst.png"))
        self.mapImages.append(tk.PhotoImage(file="maps/monza.png"))
        self.mapImages.append(tk.PhotoImage(file="maps/spa.png"))
        self.mapImages.append(tk.PhotoImage(file="maps/nurburgring.png"))
        self.mapImages.append(tk.PhotoImage(file="maps/suzuka.png"))
        self.mapImages.append(tk.PhotoImage(file="maps/watkins_glenn.png"))

        # Display the maps as clickable images
        self.mapLabels = []
        for i in range(len(self.mapImages)):
            label = tk.Label(self, image=self.mapImages[i])
            label.bind("<Button-1>", lambda event, index=i: self.onMapClick(index))
            label.grid(row = i // 2 + 2, column = i % 2)
            self.mapLabels.append(label)

        # Create a label to display the selected map
        self.selectedMapLabel = tk.Label(self, text="No map selected")

    def onMapClick(self, index):
        self.selectedMapLabel.config(text=manager.maps[index])
        self.addLap()

    def addLap(self):
        self.addLapWindow = tk.Toplevel(self.master)
        self.addLapWindow.title("Add Lap")
        self.addLapWindow.geometry("200x250")
        self.addLapWindow.resizable(False, False)
        self.addLapFrame = tk.Frame(self.addLapWindow)
        self.addLapFrame.grid()

        averageLap = manager.GetAverageLap(self.selectedMapLabel.cget("text"))
        self.averageLabel = tk.Label(self.addLapFrame, text=f"Average Lap Time: {averageLap if averageLap is not None else 'N/A'}")
        self.averageLabel.grid(row=0, column=0, columnspan=2, pady=10)

        bestLap = manager.GetBestLap(self.selectedMapLabel.cget("text"))
        self.bestLabel = tk.Label(self.addLapFrame, text=f"Best Lap Time: {bestLap if bestLap is not None else 'N/A'}")
        self.bestLabel.grid(row=1, column=0, columnspan=2, pady=10)

        self.carLabel = tk.Label(self.addLapFrame, text="Car:")
        self.carLabel.grid(row=2, column=0, pady=10)

        self.carEntry = tk.Entry(self.addLapFrame)
        self.carEntry.grid(row=2, column=1, pady=10)

        self.timeLabel = tk.Label(self.addLapFrame, text="Lap Time:")
        self.timeLabel.grid(row=3, column=0, pady=10)

        self.timeEntry = tk.Entry(self.addLapFrame)
        self.timeEntry.grid(row=3, column=1, pady=10)

        self.playerLabel = tk.Label(self.addLapFrame, text="Player:")
        self.playerLabel.grid(row=4, column=0, pady=10)

        self.playerEntry = tk.Entry(self.addLapFrame)
        self.playerEntry.grid(row=4, column=1, pady=10)

        self.addLapButton = tk.Button(self.addLapFrame, text="Add Lap", command=self.addLapToDB)
        self.addLapButton.grid(row=5, column=0, columnspan=2, pady=10)

    def addLapToDB(self):
        manager.AddLap(self.selectedMapLabel.cget("text"), self.carEntry.get(), self.timeEntry.get(), self.playerEntry.get())
        self.addLapWindow.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()