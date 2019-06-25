from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename)

print("Here are the contents of the file:")
print(target.read())

print("Now we close it.")
target.close()
