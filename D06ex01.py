import os

os.chdir("/Users/NiaVivek/Desktop/python/D02/HW02") # to change directory
print(os.getcwd()) #to get path
filenames = os.listdir() # to get the files in the directory
for name in filenames:
	if (name[-2:] == "py"):
		print(name)