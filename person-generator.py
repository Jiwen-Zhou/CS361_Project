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

	def create_click(self):
		"""
		this function reads from the selected CSV state file
		and writes data to output.csv
		"""

		#### this part needs to be edited ####
		if self.toy_choice_box.get() == "Yes":
			call(["python", "life-generator.py", "1", "2"])



		# reset the display box
		self.display_generated.delete('0', 'end')

		# create the seed for generating random numbers
		seed(datetime.now())

		# create variables
		input_file = ""
		output_file = "output.csv"
		address_array = []
		created_array = []
		max_size = 9999
		state_ac = ""
		content_type = "street address"
		current_address = ""
		counter = 0
		first_row = True

		# check if user ran program normally or passed in input CSV
		if self.passed_csv == 1:
			# run program normally

			# check if required data is provided, return if it isn't
			if len(self.s_state.get()) == 0 or len(self.s_number.get()) == 0:
				self.display_generated.insert(0, "Please make selections before creating dataset")
				return

			# create variables specific to normal program run
			total = int(self.s_number.get())

			# check which state was selected
			selected_state = self.s_state.get()

			if selected_state == "Alaska":
				input_file = "ak.csv"
				state_ac = "AK"
			elif selected_state == "Arizona":
				input_file = "az.csv"
				state_ac = "AZ"
			elif selected_state == "California":
				input_file = "ca.csv"
				state_ac = "CA"
			elif selected_state == "Colorado":
				input_file = "co.csv"
				state_ac = "CO"
			elif selected_state == "Hawaii":
				input_file = "hi.csv"
				state_ac = "HI"
			elif selected_state == "Idaho":
				input_file = "id.csv"
				state_ac = "ID"
			elif selected_state == "Montana":
				input_file = "mt.csv"
				state_ac = "MT"
			elif selected_state == "New Mexico":
				input_file = "nm.csv"
				state_ac = "NM"
			elif selected_state == "Nevada":
				input_file = "nv.csv"
				state_ac = "NV"
			elif selected_state == "Oregon":
				input_file = "or.csv"
				state_ac = "OR"
			elif selected_state == "Utah":
				input_file = "ut.csv"
				state_ac = "UT"
			elif selected_state == "Washington":
				input_file = "wa.csv"
				state_ac = "WA"
			elif selected_state == "Wyoming":
				input_file = "wy.csv"
				state_ac = "WY"
		else:
			# user passed in CSV
			row_one = True
			csv_state = ""

			# get the selected state and total from input.csv
			with open(sys.argv[1]) as input_csv:
				read_file = csv.reader(input_csv, delimiter=",")
				for row in read_file:
					# check if reader is on the header row
					if row_one is True:
						row_one = False
						continue

					csv_state = row[0]
					total = int(row[1])

			# match the state with the state csv file
			if csv_state == "AK":
				input_file = "ak.csv"
				state_ac = "AK"
			elif csv_state == "AZ":
				input_file = "az.csv"
				state_ac = "AZ"
			elif csv_state == "CA":
				input_file = "ca.csv"
				state_ac = "CA"
			elif csv_state == "CO":
				input_file = "co.csv"
				state_ac = "CO"
			elif csv_state == "HI":
				input_file = "hi.csv"
				state_ac = "HI"
			elif csv_state == "ID":
				input_file = "id.csv"
				state_ac = "ID"
			elif csv_state == "MT":
				input_file = "mt.csv"
				state_ac = "MT"
			elif csv_state == "NM":
				input_file = "nm.csv"
				state_ac = "NM"
			elif csv_state == "NV":
				input_file = "nv.csv"
				state_ac = "NV"
			elif csv_state == "OR":
				input_file = "or.csv"
				state_ac = "OR"
			elif csv_state == "UT":
				input_file = "ut.csv"
				state_ac = "UT"
			elif csv_state == "WA":
				input_file = "wa.csv"
				state_ac = "WA"
			elif csv_state == "WY":
				input_file = "wy.csv"
				state_ac = "WY"
			else:
				# print an error message to the generated data listbox
				self.display_generated.insert(0, "Incorrect data entered. Please enter your state")
				self.display_generated.insert(1, "as a two-letter abbreviation, followed by amount.")
				return

		# read the CSV file selected, created an address array to pull from
		with open(input_file) as file_data:
			read_file = csv.reader(file_data, delimiter=',')
			for row in read_file:

				# check if the reader is on the header row
				if first_row is True:
					first_row = False
					continue

				# add the current address to address array
				current_address = row[2]
				current_address += ' '
				current_address += row[3]
				address_array.append(current_address)
				counter += 1
				if counter >= max_size:
					break

			# write the data to output file, and to created_array for GUI display
			with open(output_file, mode='w', newline='') as output_csv:

				# write the header to the file
				writer = csv.writer(output_csv, delimiter=",")
				writer.writerow(("input_state", "input_number_to_generate",
								 "output_content_type", "output_content_value"))

				# write the addresses to the file
				i = 0
				while i != total:
					index = randint(0, 9999)

					# check if there's usable data retrieved
					if address_array[index][0] == '0':
						continue
					elif address_array[index].find('-') != -1:
						continue
					elif ord(address_array[index][0]) < 49 or ord(address_array[index][0]) > 57:
						continue
					elif address_array[index].find('.') != -1:
						continue
					elif len(address_array[index]) < 5:
						continue
					elif address_array[index].find('&') != -1:
						continue
					elif address_array[index] == ' ':
						continue
					elif address_array[index][len(address_array[index]) - 2] == ' ':
						continue
					elif address_array[index][len(address_array[index]) - 1] == 'E':
						continue
					elif address_array[index][len(address_array[index]) - 1] == 'W':
						continue
					elif len(address_array[index]) != 0:
						writer.writerow((state_ac, str(total), content_type, address_array[index]))
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