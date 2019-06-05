# declare string variable
formatter = "{} {} {} {}"

# display things inserted into the variable using the format function
# we are passing it four arguments to match up with the four {} in the variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
