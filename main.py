from tkinter import *
from tkinter import ttk
import application as app

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Weclome to the GT7 Lap Tracker!").grid(column=0, row=0)
ttk.Button(frm, text="Add a Circuit", command=root.destroy).grid(column=0, row=1)
ttk.Button(frm, text="Add a Player", command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text="Enter a new Lap", command=root.destroy).grid(column=0, row=3)
ttk.Button(frm, text="Circuits", command=root.destroy).grid(column=0, row=4)
ttk.Button(frm, text="Players", command=root.destroy).grid(column=0, row=5)
ttk.Button(frm, text="Fastest Laps", command=root.destroy).grid(column=0, row=6)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=0, row=7)
root.mainloop()

#
# app.run()