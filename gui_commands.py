import tkinter as tk
from tkinter import filedialog
import memory as mem

m = mem.Memory()

def open_file(root):
	file = filedialog.askopenfilename(initialdir="/", title="Choose A File", filetypes=(('text files', '*.txt'),))
	if file:
		with open(file) as f:
			commandArray = f.read().splitlines()
		complete = m.load_gui(commandArray)
		complete_string = tk.StringVar()
		if complete:
			complete_string.set("***Program Loading Finished***")
		else:
			complete_string.set("There was an error please try again")

		complete_label = tk.Label(root, textvariable=complete_string)
		complete_label.grid(columnspan=3, column=0, row=2)

