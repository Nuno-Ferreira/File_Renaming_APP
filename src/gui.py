"""GUI for the application."""

from tkinter import *
from tkinter import ttk, filedialog
import os

def search_for_file_path():
    """Open a file dialog to search for a directory."""
    # Get the current directory
    currdir = os.getcwd()

    # Open a file dialog to search for a directory
    directory = filedialog.askdirectory(parent=root, initialdir=currdir, title="Select a folder:")

    # Update the folder path to be displayed
    dir_path.configure(text=directory)

root = Tk()
root.title("File Renaming App")

# Create the main frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create the entry for the name sequence
name_sequence = StringVar()
name_sequence_entry = Entry(mainframe, width=7, textvariable=name_sequence)
name_sequence_entry.grid(column=2, row=2, sticky=(W, E))

# Create the label to display the folder path
dir_path = Label(mainframe, text="")
dir_path.grid(column=2, row=1, sticky=E)

# Create the buttons and labels
Label(mainframe, text="Folder Selected:").grid(column=1, row=1, sticky=E)
Button(mainframe, text="Browse", command=search_for_file_path).grid(column=3, row=1, sticky=W)
Label(mainframe, text="How would you like your files to be named?").grid(column=1, row=2, sticky=E)
Button(mainframe, text="Rename").grid(column=2, row=3, sticky=N)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

name_sequence_entry.focus()
root.bind("<Return>")

root.mainloop()
