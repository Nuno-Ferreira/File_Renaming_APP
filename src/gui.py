"""GUI for the application."""

from tkinter import *
from tkinter import ttk, filedialog
import os
from script import rename_files

def search_for_file_path() -> None:
    """Open a file dialog to search for a directory."""
    # Get the current directory
    currdir = os.getcwd()

    # Open a file dialog to search for a directory
    directory = filedialog.askdirectory(parent=root, initialdir=currdir, title="Select a folder:")

    # Update the folder path to be displayed
    dir_path.configure(text=directory)

def run_rename_files() -> None:
    """Run the rename_files function and update the status label."""
    directory = dir_path.cget("text")
    new_name = name_sequence.get()

    if directory and new_name:
        rename_files(directory, new_name)
        status_label.config(text="Files have been renamed successfully!", fg="green", font=("Arial", 12, "bold"))
    else:
        status_label.config(text="Please select a directory and enter a name.", fg="red", font=("Arial", 12, "bold"))

def center_window(root, width=700, height=150):
    """Center the Tkinter window on the screen."""
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the Tkinter window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the geometry of the window with the calculated values
    root.geometry(f"{width}x{height}+{x}+{y}")

root = Tk()
root.title("File Renaming App")

# Set the window size and center it
center_window(root, width=700, height=150)

# Create the main frame
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Configure the grid to expand and center content
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

# Create the entry for the name sequence
name_sequence = StringVar()
name_sequence_entry = Entry(mainframe, width=30, textvariable=name_sequence)
name_sequence_entry.grid(column=2, row=2, columnspan=2, sticky=(W, E))

# Create the label to display the folder path
dir_path = Label(mainframe, text="", anchor="w")
dir_path.grid(column=2, row=1, columnspan=2, sticky=(W, E))

# Create the status label to display messages
status_label = Label(mainframe, text="", anchor="center")
status_label.grid(column=1, row=4, columnspan=3, sticky=(W, E))

# Create the buttons and labels
Label(mainframe, text="Folder Selected:").grid(column=1, row=1, sticky=E)
Button(mainframe, text="Browse", command=search_for_file_path).grid(column=4, row=1, sticky=W)
Label(mainframe, text="How would you like your files to be named?").grid(column=1, row=2, sticky=E)

# Link the rename button to the run_rename_files function
Button(mainframe, text="Rename", command=run_rename_files).grid(column=2, row=3, columnspan=2)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

name_sequence_entry.focus()
root.bind("<Return>")

root.mainloop()
