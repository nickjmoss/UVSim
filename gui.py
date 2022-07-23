import tkinter as tk
import gui_commands

root = tk.Tk()
root.title("UVSim")

# Canvas width and placement on screen
frame = tk.Frame(root, width= 600, height= 500)
frame.grid(columnspan=3, rowspan=11)

# Instructions text
instructions = tk.Label(root, text="Import a txt file for UVSim to run", font="Raleway")
instructions.grid(columnspan=3, column=0, row=0)

# File browse text
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, fg="#000", font="Raleway")
browse_btn.config(command=lambda:gui_commands.open_file(printbutton, complete_label, complete_string, resetbutton))
browse_text.set("Choose a File")
browse_btn.grid(columnspan=3, column=0, row=1)

# Button to load and execute program
printbutton = tk.Button(root, text="Execute Program", fg="#000", state="disabled")
printbutton.config(command=lambda:gui_commands.run(memory_lbl, memory_widget, complete_label, printbutton, resetbutton, browse_btn))

# Reset Button
resetbutton = tk.Button(root, text="Reset Program", fg="#000", state="active")
resetbutton.config(command=lambda:gui_commands.reset(root, browse_btn, resetbutton, memory_widget, memory_lbl))

# Memnory Label
memory_lbl = tk.Label(root, fg="#000", text="Memory:")

# Program loaded label
complete_string = tk.StringVar()
complete_label = tk.Label(root, textvariable=complete_string)

# Widget for the program memory
memory_widget = tk.Text(root, height = 20, width = 100, bg="#000", fg="#FFF")
memory_widget.grid(columnspan=3, column=0, row=10)

# Integer input error message
integer_string = tk.StringVar()
integer_error_message = tk.Label(root)

root.mainloop()
