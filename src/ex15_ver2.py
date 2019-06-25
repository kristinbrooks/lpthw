# import sys module with the argument variable
from sys import argv

# assign variables to argv
script, filename = argv

# open the file given on the command line
txt = open(filename)

# display what was in the opened file using read function on opened file
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()
