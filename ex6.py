# declare variable
types_of_people = 10
# make a string with the created variable and assign it to a new variable
x = f"There are {types_of_people} types of people."

# declare variable
binary = "binary"
# declare variable
do_not = "don't"
# make a string with the created variables and assign it to a new variable
y = f"Those who know {binary} and those who {do_not}."

# display the strings
print(x)
print(y)

# display a repeat of the strings
print(f"I said : {x}")
print(f"I also said: '{y}'")

# declare variable
hilarious = False  # assigned a boolean value
# assign a string to a new variable with a place for an as yet unknown variable to be inserted
joke_evaluation = "Isn't that joke so funny?! {}"

# print the new string with the boolean variable inserted
print(joke_evaluation.format(hilarious))

# declare new variables
w = "This is the left side of..."
e = "a string with a right side."

# display the addition of the new strings
print(w + e)
