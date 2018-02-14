'''
Cellular Automation, an array of cells that turn on/off based on whether other cells are on/off
Program will print out an image in PBF
Takes in two parameters: rule number, number of row 
'''

import sys

rule = int(sys.argv[1])
row = int(sys.argv[2]) #row
row_length = int(sys.argv[2]) * 2 + 1

BITS = 8

# Set the rule
def set_rule(n):
	binary_number_list = []
	binary_number=bin(int(n))[2:].zfill(BITS) #String
	for count0 in binary_number:
		binary_number_list.append(count0)
	reverse_binary_number_list = binary_number_list[::-1]
	return reverse_binary_number_list

def initial_row(x):
	print("P1", row_length, row, sep= ' ') 

	middle = int((row_length - 1)/2)
	current_string = ""
	for i in range(row_length):
		if (i == middle):
			current_string += "1"
		else:
			current_string += "0"
	print(current_string)
	return current_string

# map to placement 
def all_rows(rules, rows):
	previous_row = initial_row(rule)
	current_string = ""

	# Append 1 or 0 based previous row
	# Account for sides
	while rows > 0:
		# Begin at 0
		for x in range(row_length):
			# L
			if x == 0:
				binary_set = '0' + str(previous_row[x:2])
				# print("This is the binary set ",binary_set)
				value = int(binary_set, 2)
				current_string += set_rule(rules)[value]
			elif x == row_length - 1:
				binary_set = str(previous_row[x:2]) + "0"
				value = int(binary_set, 2)
				current_string += set_rule(rules)[value]
			else:
				binary_set = str(previous_row[x - 1 : x + 2])
				# print("This is",binary_set)
				value = int(binary_set, 2)
				current_string += set_rule(rules)[value]
		print(current_string)
		rows -= 1
		previous_row = current_string
		current_string = ""

def main():
	all_rows(rule, row)
	# print(set_rule(rule))

main()