#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports
import HW06_ch09_ex02 as read_script
# Body
def uses_all(word, required):
	""" return True if word NOT forbidden"""
	for letters in word:#check if each letter in the word is a required letter
		if letters.lower() not in required.lower():
			return False
	return True

def print_result():
	all_words = read_script.read_file("words.txt")
	count_words(all_words, "aeiou")
	count_words(all_words, "aeiouy")

def count_words(allwords, required):
	count_wd_with_let = 0 # counter for counting words with required letters
	for words in allwords:
		if uses_all(words.strip(), required):#if it contains the letters increase counter
			count_wd_with_let += 1
	print("Number of words with letters {} : {}".format(required, count_wd_with_let))


##############################################################################
def main():
    print_result() # Call your function(s) here.

if __name__ == '__main__':
    main()
