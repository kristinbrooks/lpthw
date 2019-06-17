# practice mixing format strings and escape sequences
stuff = "{} {} {}"

drunk = '''
Today I've drunk:
\t- Iced Tea\n\t- Iced Chai\n\t- Italian Soda
'''
eaten = '''
Today I've eaten:
\t* Ice Cream
\t* Cookie
\t* Savory \'Poptart\'
\t* Maple Sausage Wrap
'''
thoughts = "\v\v\vIt's been a delicious day so far. Yum yum!!!"

print(stuff.format(drunk, eaten, thoughts))
