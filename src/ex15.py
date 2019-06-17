# import sys module with the argument variable
from sys import argv

# assign variables to argv
script, filename = argv

# display what was in the opened file using read function on opened file
print(f"Here's your file {filename}:")
txt = open(filename)
print(txt.read())

# ask for the filename that was given on the command line again
print("Type the filename again:")
file_again = input(">")

# open the file again
txt_again = open(file_again)

# display the file again using read function on opened file
print(txt_again.read())
