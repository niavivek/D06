# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(nestedlists):
	total_lists = 0 # variable to store total
	for numbers in nestedlists:
		if type(numbers) == int:# if the type is int - sum function does not work on it
		#just add the value to the total
			total_lists += numbers
		else:#recursively calls the function passing the list
			total_lists += nested_sum(numbers)
	return total_lists

	

##############################################################################
def main():
    # print(nested_sum([1,2,[3]]))
    # print(nested_sum([[[1,2],[3]],[3,4]]))
    # print(nested_sum([[1,2],[2,3],[4,5]]))
    pass

if __name__ == '__main__':
    main()