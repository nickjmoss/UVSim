import tkinter as tk
import memory as mem
import execute
from tkinter import filedialog
import gui_commands

m = mem.Memory()
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
browse_btn = tk.Button(root, textvariable=browse_text, fg="#000", font="Raleway", command=lambda:gui_commands.open_file(root=root))
browse_text.set("Choose a File")
browse_btn.grid(column=1, row=1)


# def run():
#     m.reset()
#     clear_widget(memory_widget)
#     inp = inputtxt.get(1.0, "end-1c")
#     success = m.load_gui(inp)
#     if success is False:
#         error_message.config(fg="#A00")
#         memory_lbl.grid_forget()
#         memory_widget.grid_forget()
#         return
#     error_message.config(fg="#F0F0F0")
#     execute.execute(m)

#     memory_lbl.grid(columspan= 3, column=0, row=8)
#     memory_widget.config(state="disabled")
#     m.read_gui(memory_widget)

# def clear_widget(text_widget):
#     text_widget.config(state="normal")
#     text_widget.delete(1.0,tk.END)

# # Label for instructions
# tk.Label(root, fg="#009", text=
#         "Welcome to UVSim\n"
#         "Enter your program below. Enter each word / instruction on a newline."
#     ).grid(columnspan=3, column=0, row=0)
# # Label and text box for user input
# tk.Label(root, fg= "#000", text="Console:").grid(columnspan=3, column=0, row=6)
# inputtxt = tk.Text(root, height = 5, width = 20, fg="#FFF", bg="#000")
# inputtxt.grid()

# # Button to load and execute program
# printbutton = tk.Button(root, text="Execute Program", fg="#000", command=run)
# printbutton.grid(columnspan=3, column=0, row=7)

# error_message = tk.Label(root, text="Invalid Entry. Re-enter program.", fg="#F0F0F0")
# error_message.grid()

# memory_lbl = tk.Label(root, fg="#000", text="Memory:")
# # Widget for the program memory
# memory_widget = tk.Text(root, height = 5, width = 20, bg="#000", fg="#FFF")


root.mainloop()
