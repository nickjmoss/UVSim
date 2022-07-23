import tkinter as tk
from tkinter import filedialog
import memory as mem
import execute

m = mem.Memory()

def open_file(printbutton, complete_label, complete_string, resetbutton):
	resetbutton.grid_forget()
	printbutton.grid(columnspan=3, column=0, row=3)
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

def run(memory_lbl, memory_widget, complete_label, printbutton, resetbutton, browse_btn):
	browse_btn["state"] = "disabled"
	complete_label.grid_forget()
	printbutton.grid_forget(),
	resetbutton.grid(columnspan=3, column=0, row=3)
	clear_widget(memory_widget)
	execute.execute(m)
	memory_lbl.grid(columnspan= 2, column=0, row=5)
	memory_widget.config(state="disabled")
	m.read_gui(memory_widget)


def reset(root, browse_btn, resetbutton, memory_widget, memory_lbl):
	m.reset()
	delete = [".contents", "int_lbl", "inputtxt", "printbutton"]
	try:
		for name in delete:
			if root.nametowidget(name):
				root.nametowidget(name).grid_forget()
	except KeyError:
		print("Widgets do not exist")
	resetbutton.grid_forget()
	memory_lbl.grid_forget()
	clear_widget(memory_widget)
	browse_btn["state"] = "active"