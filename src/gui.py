"""GUI for the application."""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("File Renaming App")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name_sequence = StringVar()
name_sequence_entry = ttk.Entry(mainframe, width=7, textvariable=name_sequence)
name_sequence_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Rename").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="How would you like your files to be named?").grid(column=1, row=1, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

name_sequence_entry.focus()
root.bind("<Return>")

root.mainloop()