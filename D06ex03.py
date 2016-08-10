
"""Reads a file and determines and prints the names with e"""
def read_file(filename):
	file_to_read = open(filename, 'r')#open the file for reading
	#variable to store names with 'e'
	all_names_with_e = []
	#counter to count the number of names with 'e'
	count_names = 0
	# read the lines as a list
	names_to_print = file_to_read.readlines()
	#iterate through the list
	for names in names_to_print:
		firstname = names.split()#split the first name from the line
		if('e' in firstname[0]):#if frstname has 'e'
			count_names += 1 #increase count
			all_names_with_e.append(firstname[0])#append the name to the list
		#print count and names
	print("Number of names with e: {}".format(count_names))
	for name in all_names_with_e:
		print(name)
	file_to_read.close()
##############################################################################
def main():
    read_file("roster.txt")

if __name__ == '__main__':
    main()