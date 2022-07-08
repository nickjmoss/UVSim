from tkinter import *
from memory import *
from execute import *

root = Tk()
m = Memory()
root.title("UVSim")
root.geometry("500x500")

def run():
    inp = inputtxt.get(1.0, "end-1c")
    m.load_program(inp, root)

    execute(m)

    Label(root, fg="#000", text="Memory:").pack()
    m.read_program(root)

Label(root, fg="#009", text=
        "Welcome to UVSim\n"
        "Enter your program below. Enter each word / instruction on a newline."
    ).pack()
Label(root, fg= "#000", text="Console:").pack()
inputtxt = Text(root, height = 5, width = 20, fg="#fff")
inputtxt.pack()

printbutton = Button(root, text="Execute Program", fg="#000", command=run)
printbutton.pack()

lbl = Label(root, text = "")
lbl.pack()

root.mainloop()
