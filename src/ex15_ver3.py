# ask for the filename from the user
print("Type the filename you'd like to open:")
filename = input(">")

# open the file
txt = open(filename)

# use the read function to display the txt in the opened file
print(txt.read())

txt.close()
