import tkinter as tk
from tkinter import filedialog
from turtle import clear

from matplotlib.pyplot import text
import memory as mem
import execute

m = mem.Memory()

def open_file(printbutton, complete_label, complete_string):
	m.reset()
	file = filedialog.askopenfilename(initialdir="/", title="Choose A File", filetypes=(('text files', '*.txt'),))
	if file:
		with open(file) as f:
			commandArray = f.read().splitlines()
		complete = m.load_gui(commandArray)
		complete_label.grid(columnspan=3, column=0, row=2)
		if complete:
			complete_string.set("***Program Loading Complete***")
			printbutton["state"] = "active"
		else:
			printbutton["state"] = "disabled"
			complete_string.set("There was a problem loading the commands")
		

def clear_widget(text_widget):
	text_widget.config(state="normal")
	text_widget.delete(1.0,tk.END)

def run(memory_lbl, memory_widget, complete_label):
	complete_label.grid_forget()
	clear_widget(memory_widget)
	execute.execute(m)
	memory_lbl.grid(columnspan= 2, column=0, row=5)
	memory_widget.config(state="disabled")
	m.read_gui(memory_widget)