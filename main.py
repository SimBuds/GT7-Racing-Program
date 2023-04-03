from manager import Manager
from tkinter import *
from tkinter import messagebox

manager = Manager()
manager.CreateDB()

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("GT7 Lap Time Tracker")
        self.master.geometry("300x300")
        self.master.resizable(True, True)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.btn1 = Button(self.frame, text="Add", width=10, height=2, command=self.add)
        self.btn1.grid(row=0, column=0, padx=5, pady=5)
        self.btn2 = Button(self.frame, text="Remove", width=10, height=2, command=self.remove)
        self.btn2.grid(row=0, column=1, padx=5, pady=5)
        self.btn3 = Button(self.frame, text="Search", width=10, height=2, command=self.search)
        self.btn3.grid(row=0, column=2, padx=5, pady=5)
        self.btn4 = Button(self.frame, text="Show All", width=10, height=2, command=self.show_all)
        self.btn4.grid(row=1, column=0, padx=5, pady=5)
        self.btn5 = Button(self.frame, text="Exit", width=10, height=2, command=self.exit)
        self.btn5.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    def add(self):
        self.newWindow = Toplevel(self.master)
        self.app = Add(self.newWindow)

    def remove(self):
        self.newWindow = Toplevel(self.master)
        self.app = Remove(self.newWindow)

    def search(self):
        self.newWindow = Toplevel(self.master)
        self.app = Search(self.newWindow)

    def show_all(self):
        self.newWindow = Toplevel(self.master)
        self.app = DisplayResults(self.newWindow)

    def exit(self):
        self.master.destroy()

class Add:
    def __init__(self, master):
        self.master = master
        self.master.title("Add A Lap")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.lbl1 = Label(self.frame, text="Name")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        self.entName = Entry(self.frame, width=20)
        self.entName.grid(row=0, column=1, padx=5, pady=5)
        self.lbl2 = Label(self.frame, text="Map")
        self.lbl2.grid(row=1, column=0, padx=5, pady=5)
        self.entMap = Entry(self.frame, width=20)
        self.entMap.grid(row=1, column=1, padx=5, pady=5)
        self.lbl3 = Label(self.frame, text="Lap Time")
        self.lbl3.grid(row=2, column=0, padx=5, pady=5)
        self.entTime = Entry(self.frame, width=20)
        self.entTime.grid(row=2, column=1, padx=5, pady=5)
        self.btn1 = Button(self.frame, text="Add", width=10, height=2, command=self.add)
        self.btn1.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def add(self):
        if self.entName.get() == "" or self.entMap.get() == "" or self.ent3.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            manager.AddLap(self.ent1.get(), self.entMap.get(), self.ent3.get())
            messagebox.showinfo("Success", "Lap added successfully")
            self.master.destroy()

class Remove:
    def __init__(self, master):
        self.master = master
        self.master.title("Remove A Lap")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.lbl1 = Label(self.frame, text="Name")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        self.ent1 = Entry(self.frame, width=20)
        self.ent1.grid(row=0, column=1, padx=5, pady=5)
        self.lbl2 = Label(self.frame, text="Map")
        self.lbl2.grid(row=1, column=0, padx=5, pady=5)
        self.ent2 = Entry(self.frame, width=20)
        self.ent2.grid(row=1, column=1, padx=5, pady=5)
        self.lbl3 = Label(self.frame, text="Lap Time")
        self.lbl3.grid(row=2, column=0, padx=5, pady=5)
        self.ent3 = Entry(self.frame, width=20)
        self.ent3.grid(row=2, column=1, padx=5, pady=5)
        self.btn1 = Button(self.frame, text="Remove", width=10, height=2, command=self.remove)
        self.btn1.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def remove(self):
        if self.ent1.get() == "" or self.ent2.get() == "" or self.ent3.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            manager.RemoveLap(self.ent1.get(), self.ent2.get(), self.ent3.get())
            messagebox.showinfo("Success", "Lap removed successfully")
            self.master.destroy()

class Search:
    def __init__(self, master):
        self.master = master
        # Name of the window
        self.master.title("Search For a Lap")
        # Size of the window
        self.master.geometry("300x300")
        # Disable resizing the GUI
        self.master.resizable(False, False)
        # Create a frame
        self.frame = Frame(self.master)
        # Pack the frame
        self.frame.pack()
        # Create a label
        self.lbl1 = Label(self.frame, text="Name")
        # Place the label
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        # Create an entry
        self.ent1 = Entry(self.frame, width=20)
        self.ent1.grid(row=0, column=1, padx=5, pady=5)
        self.lbl2 = Label(self.frame, text="Map")
        self.lbl2.grid(row=1, column=0, padx=5, pady=5)
        self.ent2 = Entry(self.frame, width=20)
        self.ent2.grid(row=1, column=1, padx=5, pady=5)
        self.btn1 = Button(self.frame, text="Search", width=10, height=2, command=self.search)
        self.btn1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def search(self):
        # Check if the entries are empty
        if self.ent1.get() == "" or self.ent2.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            self.newWindow = Toplevel(self.master)
            # Sending the entries to the next window that uses .get() to get the values
            self.app = SearchResults(self.newWindow, self.ent1.get(), self.ent2.get())

class SearchResults:
    def __init__(self, master, name, map):
        self.master = master
        self.master.title("Search Results")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.lbl1 = Label(self.frame, text="Name")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        self.lbl2 = Label(self.frame, text="Map")
        self.lbl2.grid(row=0, column=1, padx=5, pady=5)
        self.lbl3 = Label(self.frame, text="Lap Time")
        self.lbl3.grid(row=0, column=2, padx=5, pady=5)
        self.lbl4 = Label(self.frame, text=name)
        self.lbl4.grid(row=1, column=0, padx=5, pady=5)
        self.lbl5 = Label(self.frame, text=map)
        self.lbl5.grid(row=1, column=1, padx=5, pady=5)
        self.lbl6 = Label(self.frame, text=manager.SearchLap(name, map))
        self.lbl6.grid(row=1, column=2, padx=5, pady=5)

class Display:
    def __init__(self, master):
        self.master = master
        self.master.title("Display")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.lbl1 = Label(self.frame, text="Name")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        self.ent1 = Entry(self.frame, width=20)
        self.ent1.grid(row=0, column=1, padx=5, pady=5)
        self.btn1 = Button(self.frame, text="Display", width=10, height=2, command=self.display)
        self.btn1.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def display(self):
        if self.ent1.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            self.newWindow = Toplevel(self.master)
            self.app = DisplayResults(self.newWindow, self.ent1.get())

class DisplayResults:
    def __init__(self, master, name):
        self.master = master
        self.master.title("Display Results")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.frame = Frame(self.master)
        self.frame.pack()
        self.lbl1 = Label(self.frame, text="Name")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)
        self.lbl2 = Label(self.frame, text="Map")
        self.lbl2.grid(row=0, column=1, padx=5, pady=5)
        self.lbl3 = Label(self.frame, text="Lap Time")
        self.lbl3.grid(row=0, column=2, padx=5, pady=5)
        self.lbl4 = Label(self.frame, text=name)
        self.lbl4.grid(row=1, column=0, padx=5, pady=5)
        self.lbl5 = Label(self.frame, text=manager.DisplayLap(name))
        self.lbl5.grid(row=1, column=1, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    app = Main(master=root)
    app.mainloop()