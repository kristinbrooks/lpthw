# practice asking questions
print('What is your first name?:', end='')
first_name = input()
print('What is your last name?:', end='')
last_name = input()

# same questions with new line for user input
#print('What is your first name?:')
#first_name = input()
#print('What is your last name?:')
#last_name = input()

# display entered info
print('\nSo your name is', first_name, '{}.'.format(last_name))
# alternate format
print('\nSo your name is', first_name, last_name, '.')  # EXTRA SPACE BEFORE PERIOD???

# get user to hit enter to get next sequence of questions
print('\vPlease hit enter.')
input()

# more questions
salary = int(input('How much money do you make a month? '))
expenses = int(input('How much are your monthly expenses? '))

# same questions with new line for user input
#salary = int(input('How much money do you make a month?\n'))
#expenses = int(input('How much are your monthly expenses?\n'))


# tell the user how much money they have left over each month
print('\v{}, based on that information, you have'.format(first_name), salary - expenses, 'dollars left to spend each month.')

# alternate format to get same sentence displayed
#print(f'\v{first_name}, based on that information, you have {salary - expenses} dollars left to spend each month.')
