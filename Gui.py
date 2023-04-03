import tkinter as tk
from tkinter import ttk
from manager import Manager  # Changed the import statement

manager = Manager()
manager.CreateDB()

class Main(tk.Frame):  # Main should inherit from tk.Frame
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("GT7 Lap Time Tracker")
        self.master.geometry("400x450")
        self.master.resizable(False, False)
        self.master.config(bg="#d9d9d9")
        self.grid()

        self.lbl1 = tk.Label(self, text="GT7 Lap Time Tracker")
        self.lbl1.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.mapLabel = tk.Label(self, text="Choose a map:")
        self.mapLabel.grid(row=1, column=0, columnspan=2, pady=10)

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
            label.grid(row=i // 2 + 2, column=i % 2)
            self.mapLabels.append(label)

        # Create a label to display the selected map
        self.selectedMapLabel = tk.Label(self, text="No map selected")
        self.selectedMapLabel.grid(row=4, column=0, columnspan=2, pady=10)

    def onMapClick(self, index):
        self.selectedMapLabel.config(text=manager.maps[index])  # Reference the map name from the manager object

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()