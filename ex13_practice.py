from sys import argv
script, your_name, phone_type = argv

address = input('What is your street address? ')
city = input('What city do you live in? ')
state = input('What state do you live in? ')
zip = input('What is your zip code?')

print(your_name, f', your full address is: \n{address}\n{city}, {state}, zip')

phone_number = input('What is your phone number? ')

print(f'You have an {phone_type} and its number is {phone_number}.')
