import tkinter as tk
from tkinter import filedialog
import gui_commands

root = tk.Tk()
root.title("UVSim")

# Canvas width and placement on screen
canvas = tk.Canvas(root, width= 600, height= 500)
canvas.grid(columnspan=3, rowspan=10)

# Instructions text
instructions = tk.Label(root, text="Import a txt file for UVSim to run", font="Raleway")
instructions.grid(columnspan=3, column=0, row=0)

# File browse text
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, fg="#000", font="Raleway", command=lambda:gui_commands.open_file(root, printbutton))
browse_text.set("Choose a File")
browse_btn.grid(columnspan=3, column=0, row=1)

# Button to load and execute program
printbutton = tk.Button(root, text="Execute Program", fg="#000", command=lambda:gui_commands.run(memory_lbl, memory_widget), state="disabled")
printbutton.grid(columnspan=3, column=0, row=3)

error_message = tk.Label(root, text="Invalid Entry. Re-enter program.", fg="#F0F0F0")

memory_lbl = tk.Label(root, fg="#000", text="Memory:")

# Widget for the program memory
memory_widget = tk.Text(root, height = 20, width = 100, bg="#000", fg="#FFF")


root.mainloop()
