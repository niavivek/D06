#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports
import HW06_ch09_ex02 as read_script
# Body
def is_abededarian(word):
	prev_let = word[0] #get the first word as previous letter
	for letters in word: # iterate through letters
		if ord(letters.lower()) < ord(prev_let.lower()):#compare ASCII values
			return False # return false if second letter is of lower ASCII value
			# or out of alphabetical value
		prev_let = letters # assign the current letter as previous letter
		# for next iteration
	return True

def abededarian_count():
	# get the words from the file
	all_words = read_script.read_file("words.txt")
	count_abede = 0 #initialize counter
	for words in all_words:#iterate through words
		if is_abededarian(words.strip()): #if letter appear in order
			count_abede += 1 #increase count
	print("Number of abededarian words : {}".format(count_abede)) # print count

##############################################################################
def main():
    abededarian_count() # Call your function(s) here.

if __name__ == '__main__':
    main()
