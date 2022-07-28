'''
Author: Melissa Dunn
'''
import re
import tkinter as tk

class IO:
	def read(self, location, memory):
		'''Read a word from the keyboard into a specific location in memor'''

		while True:
			print("Enter an integer: ", end="")

			user_input = input()

			if(re.fullmatch("^[+-]?\d{1,6}", user_input) is None):
				print("Invalid input. Try again.")
			else:
				break

		
		memory.store(location, (user_input).zfill(5))
		if user_input.startswith("-"):
			user_input = (user_input).zfill(5)
			user_input = user_input.replace("-","1")
		else:
			user_input = user_input.replace("+", "0")
		memory.store(location, (user_input).zfill(5))


	def write(self, location, memory):
		'''Write a word from a specific location in memory to screen.'''


		output = re.sub(r'^1', "-", memory.get(location))
		print(f"Contents of {int(location)} is {int(output)}")

	def read_gui(self, location, memory):
		'''Read a word from the keyboard into a specific location in memory'''
		loop_bool = True
		def enter(wait):
			nonlocal loop_bool

			wait.set(1)
			user_input = inputtxt.get(1.0, "end-1c")


			if re.fullmatch("^[+-]?\d{1,4}", user_input) is None:
				loop_bool = True
			else:
				if user_input.startswith("-"):
					user_input = (user_input).zfill(5)
					user_input = user_input.replace("-","1")
				else:
					user_input = user_input.replace("+", "0")
				memory.store(location, user_input)
				loop_bool = False
		
		while loop_bool:
			integer_label = tk.Label(name="int_lbl", fg="#000", text=f"Enter an integer for location {location}:")
			integer_label.grid(columnspan=1, column=0, row=4)
			inputtxt = tk.Text(height = 1, width = 5, fg="black", bg="white", name="inputtxt")
			inputtxt.config(highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
			inputtxt.grid(columnspan=1, column=1, row=4)
			wait_var = tk.IntVar()
			printbutton = tk.Button(text="Enter", fg="#000", command=lambda:enter(wait_var), name="printbutton")
			printbutton.grid(columnspan=1, column=2, row=4)
			printbutton.wait_variable(wait_var)


	def write_gui(self, location, memory):
		'''Write a word from a specific location in memory to screen.'''
		output = re.sub(r'^1', "-", memory.get(location))
		tk.Label(fg="green", text=f"Contents of {int(location)} is {int(output)}", name="contents").grid(columnspan=1, column=2, row=5)
