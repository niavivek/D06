import random

def write_random_numbers(size, start, end):
	#open the file for write
	file_to_write = open("test1.txt", 'w')

# creates a list of 10 random numbers in the range 1 to 1000
	numbers_to_write = random.sample(range(start, end), size) 
#write the list to the file
	for n in numbers_to_write:
		file_to_write.write(str(n) + "\n")
#close the file
	file_to_write.close()

##############################################################################
def main():
    write_random_numbers(10, 1, 1000)

if __name__ == '__main__':
    main()