# Zach Marcus
# CS 361
# Person Generator Project
#
# =======================================================
# This program takes a selected state along with an amount and generates
# a list of random addresses from that state, outputting the list
# into a csv file and displaying the generated data in the GUI.
# The selected state and amount can also be passed in through the command line.
# If using the command line, the layout of the input csv file must be state followed
# by number of addresses to generate. State csv files can be downloaded in from
# https://www.kaggle.com/openaddresses/openaddresses-us-west?select=nm.csv
# Note: state csv files must be in the directory in order to generate the necessary
# data.
# =======================================================
import tkinter as tkinter
import tkinter.ttk
import csv
from random import seed
from random import randint
from datetime import datetime
import sys
from subprocess import call


class MainWindow:
	"""
	this class has all the functions for the main window
	used in the program
	"""
	def __init__(self, passed_csv):
		self.window = tkinter.Tk()
		self.window.geometry("850x500")
		self.passed_csv = passed_csv
		self.toys_selected = False

		# widget creation
		self.create_button = tkinter.Button(text="Create Dataset", font=(None, 12), height=3, width=30,
											command=self.create_click)
		self.title = tkinter.Label(text="Person Linear", font=(None, 28), width=27, height=4)
		self.s_state_label = tkinter.Label(text="Select State")
		self.s_state = tkinter.ttk.Combobox(self.window, width=27, state="readonly")
		self.s_state["values"] = ("Alaska", "Arizona", "California", "Colorado", "Hawaii",
								  "Idaho", "Montana", "New Mexico", "Nevada", "Oregon",
								  "Utah", "Washington", "Wyoming")
		self.s_number_label = tkinter.Label(text="Select Amount to Generate")
		self.s_number = tkinter.ttk.Combobox(self.window, width=27, state="readonly")
		self.s_number["values"] = ("10", "20", "30", "40", "50", "100", "200")
		self.display_generated = tkinter.Listbox(width=50, height=13)
		self.display_label = tkinter.Label(text="Generated Data:")
		self.input_received = tkinter.Label(text="Input CSV File Received!", font=(None, 18), fg="Green")
		self.toy_label = tkinter.Label(text="Display Types of Toys sent to Addresses:")
		self.toy_choice_box = tkinter.ttk.Combobox(self.window, width=27, state="readonly")
		self.toy_choice_box["values"] = ("Yes", "No")

		# standard widget placement
		self.create_button.place(x=460, y=350)
		self.title.place(x=-135, y=0)
		self.display_generated.place(x=450, y=110)
		self.display_label.place(x=450, y=81)
		self.toy_label.place(x=50, y=270)
		self.toy_choice_box.place(x=50, y=295)

		# widget placement depending on csv file passed
		if passed_csv == 1:
			# place the options allowing the user to select state and amount
			self.s_state_label.place(x=50, y=150)
			self.s_state.place(x=50, y=175)
			self.s_number_label.place(x=50, y=210)
			self.s_number.place(x=50, y=230)
		else:
			self.input_received.place(x=47, y=175)

	def read_file(self, input_file, array, file_type):
		"""
		this functions reads from the passed file (file_name)
		and writes appropriate data to array (array)
		"""
		counter = 0
		first_row = True

		# read the CSV file selected, created an address array to pull from
		with open(input_file) as file_data:
			read_file = csv.reader(file_data, delimiter=',')
			for row in read_file:

				# check if the reader is on the header row
				if first_row is True:
					first_row = False
					continue

				if file_type == "address_file":
					# add the current address to address array
					current_address = row[2]
					current_address += ' '
					current_address += row[3]
					array.append(current_address)
					counter += 1
				elif file_type == "input_csv":
					array.append(row[0])
					array.append(row[1])
				elif file_type == "toy_file":
					array.append(row[0])
					counter += 1

				if counter >= 9999:
					break

	def set_state(self, selected_state):
		"""
		this function sets the proper values for
		the input_file and state_ac variables depending
		on what's passed for selected
		"""
		if selected_state == "Alaska":
			return "ak.csv", "AK"
		elif selected_state == "Arizona":
			return "az.csv", "AZ"
		elif selected_state == "California":
			return "ca.csv", "CA"
		elif selected_state == "Colorado":
			return "co.csv", "CO"
		elif selected_state == "Hawaii":
			return "hi.csv", "HI"
		elif selected_state == "Idaho":
			return "id.csv", "ID"
		elif selected_state == "Montana":
			return "mt.csv", "MT"
		elif selected_state == "New Mexico":
			return "nm.csv", "NM"
		elif selected_state == "Nevada":
			return "nv.csv", "NV"
		elif selected_state == "Oregon":
			return "or.csv", "OR"
		elif selected_state == "Utah":
			return "ut.csv", "UT"
		elif selected_state == "Washington":
			return "wa.csv", "WA"
		elif selected_state == "Wyoming":
			return "wy.csv", "WY"
		else:
			# print an error message to the generated data listbox
			self.display_generated.insert(0, "Incorrect data entered.")

	def check_index(self, index):
		"""
		this function takes an index in an array and checks
		if it has usable data
		"""
		if index == 0:
			return False
		elif index.find('-') != -1:
			return False
		elif ord(index[0]) < 49 or ord(index[0]) > 57:
			return False
		elif index.find('.') != -1:
			return False
		elif len(index) < 5:
			return False
		elif index.find('&') != -1:
			return False
		elif index == ' ':
			return False
		elif index[len(index) - 2] == ' ':
			return False
		elif index[len(index) - 1] == 'E':
			return False
		elif index[len(index) - 1] == 'W':
			return False
		elif len(index) != 0:
			return True

	def create_click(self):
		"""
		this function reads from the selected CSV state file
		and writes data to output.csv
		"""

		# reset the display box
		self.display_generated.delete('0', 'end')

		# create variables + seed
		seed(datetime.now())
		output_file = "output.csv"
		csv_input_array = []
		address_array = []
		created_array = []
		toy_array = []
		content_type = "street address"

		# check if user wants to see what toys were sent to addresses
		if self.toy_choice_box.get() == "Yes":
			self.toys_selected = True
			call(["python", "life-generator.py", "1", "2"])
			self.read_file("output.csv", toy_array, "toy_file")

		# check if program was run normally or by command line
		if self.passed_csv == 1:
			# check if required data is provided, return if it isn't
			if len(self.s_state.get()) == 0 or len(self.s_number.get()) == 0 or \
			   len(self.toy_choice_box.get()) == 0:
				self.display_generated.insert(0, "Please make selections before creating dataset")
				return

			# create variables specific to normal program
			total = int(self.s_number.get())
			selected_state = self.s_state.get()
			input_file, state_ac = self.set_state(selected_state)
		else:
			# get the selected state and total from input.csv
			self.read_file(sys.argv[1], csv_input_array, file_type="input_csv")
			csv_state = csv_input_array[0]
			total = int(csv_input_array[1])

			# match the state with the state csv file
			input_file, state_ac = self.set_state(csv_state)

		# read the CSV file selected, put addresses into address_array
		self.read_file(input_file, address_array, file_type="address_file")

		# write the data to output file, and to created_array for GUI display
		with open(output_file, mode='w', newline='') as output_csv:

			# write the header to the file
			writer = csv.writer(output_csv, delimiter=",")

			# check if toy category row needs to be written
			if self.toys_selected is False:
				writer.writerow(("input_state", "input_number_to_generate",
								 "output_content_type", "output_content_value"))
			else:
				writer.writerow(("input_state", "input_number_to_generate",
								 "output_content_type", "output_content_value",
								 "toy_delivered"))

			# write the addresses to the file
			i = 0
			while i != total:
				index = randint(0, 9999)

				if self.check_index(address_array[index]) is True:
					if self.toys_selected is False:
						writer.writerow((state_ac, str(total), content_type, address_array[index]))
						created_array.append(address_array[index])
					else:
						writer.writerow((state_ac, str(total), content_type, address_array[index],
										 toy_array[len(toy_array) % 10]))
						created_array.append(address_array[index])
					i += 1

		# display the generated data in the GUI
		array_size = len(created_array)
		while array_size != 0:
			self.display_generated.insert(0, created_array[array_size - 1])
			array_size -= 1


def main():
	"""
	main function for executing the program
	"""

	# check if user passed in CSV file as an argument
	if len(sys.argv) == 1:
		root = MainWindow(1)
		root.window.mainloop()
	elif len(sys.argv) == 2:
		root = MainWindow(2)
		root.window.mainloop()
	else:
		root = MainWindow(1)
		root.toy_choice_box.set("No")
		root.s_state.set("Alaska")
		root.s_number.set(10)
		root.create_click()


main()