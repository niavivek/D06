#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
	#return true is e is in the word
	if 'e' in word:
		return True
	else:
		return False

def print_no_e(all_words):
	count_words_no_e = 0 # counter for words with 'e'
	total = len(all_words) #total number of words
	for word in all_words:
		if 'e' in word:
			pass
		else: # is word contains no 'e' print it
			count_words_no_e += 1
			print(word.strip())
	percent = count_words_no_e * 100 / total
	print("Percentage of word with no e: " + str(round(percent,2)) + "%")

def read_file(filename):
	file_to_read = open(filename, 'r')#open the file for reading
	#store the file's contents
	file_contents =  file_to_read.readlines()
	#close the file
	file_to_read.close()
	return file_contents

def pass_words_to_func(all_words):
	#iterate through the list and call the function to check for e
	for word in all_words:
		print(word.strip(), " contains 'e': ", has_no_e(word))
	print_no_e(all_words)

def func_calls(filename):
	#read the contents of the file and pass it to the calling function
	pass_words_to_func(read_file(filename))

##############################################################################
def main():
    func_calls("words.txt")

if __name__ == '__main__':
    main()
