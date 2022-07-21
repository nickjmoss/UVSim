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
			user_input = user_input.replace("-","")
			user_input = (user_input).zfill(5)
			user_input = str(int(user_input) * -1)
		else:
			user_input = user_input.replace("+", "0")
		memory.store(location, (user_input).zfill(5))


	def write(self, location, memory):
		'''Write a word from a specific location in memory to screen.'''

		output = re.sub(r'^1', "-", memory.memory_dict[location])
		output = re.sub(r'^1', "-", memory.get(location))
		print(f"Contents of {int(location)} is {int(output)}")

	def read_gui(self, location, memory):
		error_message = tk.Label(fg="#F0F0F0", text="Invalid input. Try again.")

		'''Read a word from the keyboard into a specific location in memory'''
		def enter(wait):
			wait.set(1)
			user_input = inputtxt.get(1.0, "end-1c")

			if(re.fullmatch("^[+-]?\d{1,4}", user_input) is None):
				error_message.config(fg="#A00")
				return
			else:
				error_message.config(fg="#F0F0F0")

			user_input = user_input.replace("+", "0").replace("-", "1")
			memory.store(location, user_input)
		tk.Label(fg="#000", text="Enter an integer:").grid()
		inputtxt = tk.Text(height = 1, width = 5, fg="#fff")
		inputtxt.grid()

		wait_var = tk.IntVar()
		printbutton = tk.Button(text="Enter", fg="#000", command=lambda:enter(wait_var))
		error_message.grid()
		printbutton.grid()
		printbutton.wait_variable(wait_var)

	def write_gui(self, location, memory):
		'''Write a word from a specific location in memory to screen.'''
		output = re.sub(r'^1', "-", memory.get(location))
		tk.Label(fg="#000", text=f"Contents of {int(location)} is {int(output)}").grid()
