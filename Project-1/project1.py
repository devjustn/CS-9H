'''

Cellular Automation, an array of cells that turn on/off based on whether other cells are on/off
Program will print out an image in PBF
Takes in two parameters: rule number, number of steps 

'''

import sys

rule = int(sys.argv[1])
steps = int(sys.argv[2]) #row
BITS = 8

# Set the rule
def set_rule(n):
	binary_number_array = []
	bin_position_values = []
	# Conversion
	binary_number=bin(int(n))[2:].zfill(BITS)
	# binary_number_array = []
	for count0 in binary_number:
		binary_number_array.append(count0)
	
	# count0 = 0
	# count1 = 0
	# for count0 in range(len(str(binary_number))):
	# 	binary_number_array.append(count0)
	for count1 in range(BITS):
		# bin_values.append(int(bin(7-count1)[2:]).zfill(3))
		bin_position_values.append(bin(int(7 - count1) )[2:].zfill(3)) # List of string containing 3 digit
	print(binary_number_array)
	print(bin_position_values)
	print(dict(zip(binary_number_array, bin_position_values))) #failed
	
	print('')
	print('')

'''
Need to share value of first, outer, last, position on first row
'''
# Init row
def initial_row(row_length):
	print("P1", rule, steps, sep = ' ') 
	middle = (rule - 1)/2
	current_string = ""
	for i in range(rule):
		if (i == middle):
			current_string += "1"
		else:
			current_string += "0"
	print(current_string)
	return current_string

def all_rows(rule, rows):
	print("")


def main():
	initial_row(rule)

main()


