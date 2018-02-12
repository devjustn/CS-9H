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

	binary_number_list = []
	# bin_position_values = []
	# # Conversion
	binary_number=bin(int(n))[2:].zfill(BITS) #String
	# # binary_number_array = []
	for count0 in binary_number:
		binary_number_list.append(count0)
	
	# count0 = 0
	# count1 = 0
	# for count0 in range(len(str(binary_number))):
	# 	binary_number_array.append(count0)
	# for count1 in range(BITS):
	# 	# bin_values.append(int(bin(7-count1)[2:]).zfill(3))
	# 	bin_position_values.append(bin(int(7 - count1) )[2:].zfill(3)) # List of string containing 3 digit
	# # print(binary_number_array)
	# print(bin_position_values)
	# print(dict(zip(binary_number_array, bin_position_values))) #failed
	#return binary number in list format
	reverse_binary_number_list = binary_number_list[::-1]
	return reverse_binary_number_list
	# print('')
	# print('')

'''
Need to share value of first, outer, last, position on first row
'''
# Init row
def initial_row(row_length):
	print("P1", rule, steps, sep = ' ') 
	middle = int((rule - 1)/2)
	current_string = ""
	for i in range(rule):
		if (i == middle):
			current_string += "1"
		else:
			current_string += "0"
	print(current_string)
	return current_string

# map to placement 
def all_rows(rule, rows):
	print("")
	current_string = ""
	previous_row = initial_row(rule)

	# Append 1 or 0 based previous row
	# Account for sides
	while rows > 0:
		# Begin at 0
		for x in range(rule):
			# print("x = " , x)
			# print("this is x" , x)
			# L *******If at first of the list
			if x == 0:
				binary_set = '0' + str(previous_row[x:2])
				# print("This is the binary set ",binary_set)
				value = int(binary_set, 2)
				# print("This is the value ", value)
				# print(set_rule(rule))
				current_string += set_rule(rule)[value]
				# print("Before: ", current_string)
				# print("This is the current string", current_string)
			elif x == rule - 1:
				binary_set = str(previous_row[x:2]) + "0"
				value = int(binary_set, 2)
				current_string += set_rule(rule)[value]
			else:
				'''

				Bad logic
				
				'''
				binary_set = str(previous_row[x - 1 : x + 2])
				# print("This is",binary_set)
				value = int(binary_set, 2)
				current_string += set_rule(rule)[value]
		print(current_string)
		rows -= 1
		current_string = ""



def main():
	all_rows(rule, steps)
	# print(set_rule(rule))

main()


