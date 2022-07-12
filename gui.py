import tkinter as tk
import memory as mem
import execute

root = tk.Tk()
m = mem.Memory()
root.title("UVSim")
root.geometry("500x500")


def run():
    m.reset()
    clear_widget(memory_widget)
    inp = inputtxt.get(1.0, "end-1c")
    success = m.load_program(inp, root)
    if success is False:
        error_message.config(fg="#A00")
        memory_lbl.pack_forget()
        memory_widget.pack_forget()
        return
    error_message.config(fg="#F0F0F0")
    execute.execute(m)

    memory_lbl.pack()
    memory_widget.config(state="disabled")
    m.read_program(memory_widget, root)

def clear_widget(text_widget):
    text_widget.config(state="normal")
    text_widget.delete(1.0,tk.END)

# Label for instructions
tk.Label(root, fg="#009", text=
        "Welcome to UVSim\n"
        "Enter your program below. Enter each word / instruction on a newline."
    ).pack()
# Label and text box for user input
tk.Label(root, fg= "#000", text="Console:").pack()
inputtxt = tk.Text(root, height = 5, width = 20, fg="#FFF", bg="#000")
inputtxt.pack()

# Button to load and execute program
printbutton = tk.Button(root, text="Execute Program", fg="#000", command=run)
printbutton.pack()

error_message = tk.Label(root, text="Invalid Entry. Re-enter program.", fg="#F0F0F0")
error_message.pack()

memory_lbl = tk.Label(root, fg="#000", text="Memory:")
# Widget for the program memory
memory_widget = tk.Text(root, height = 5, width = 20, bg="#000", fg="#FFF")

root.mainloop()
