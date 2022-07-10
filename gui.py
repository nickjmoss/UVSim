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

    def hide_memory():
        text_widget.config(state=NORMAL)
        text_widget.delete(1.0, END)
        text_widget.pack_forget()

    def display_memory():
        def print_on_gui(*args, sep=" ", end="\n"):
            text = sep.join(args) + end
            # Set the Text widget's state to normal so that we can edit its text
            text_widget.config(state="normal")
            # Insert the text at the end
            text_widget.insert("end", text)
            # Set the Text widget's state to disabled to disallow the user changing the text
            text_widget.config(state="disabled")

        # Show the widget on the screen
        text_widget.pack(fill="both", expand=True)

        cols = [str(x).zfill(2) for x in range(0,10)]
        rows = [str(x).zfill(2) for x in range(0,100,10)]

        print_on_gui("   ", end="")
        for col in cols:
            print_on_gui("{:>6}".format(col), end="")
        print_on_gui()

        for row in rows:
            print_on_gui(row, end="  ")
            for col in cols:
                position = str(int(row) + int(col)).zfill(2)
                print_on_gui(Memory.memory_dict[position], end=" ")
            print_on_gui()

    display_memory_btn.config(command=display_memory)
    display_memory_btn.pack()
    hide_memory_btn.config(command=hide_memory)
    hide_memory_btn.pack()

    # Create a new `Text` widget
    text_widget = Text(root, state="disabled")

Label(root, fg="#009", text=
        "Welcome to UVSim\n"
        "Enter your program below. Enter each word / instruction on a newline."
    ).pack()
Label(root, fg= "#000", text="Console:").pack()
inputtxt = Text(root, height = 5, width = 20, fg="#fff")
inputtxt.pack()

printbutton = Button(root, text="Execute Program", fg="#000", command=run)
printbutton.pack()

global display_memory_btn
display_memory_btn = Button(root, fg="#000", text="Display Memory")
global hide_memory_btn
hide_memory_btn = Button(root, fg="#000", text="Hide Memory")

lbl = Label(root, text = "")
lbl.pack()

root.mainloop()
