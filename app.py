## Python executes the code line by line
print('Hello Godwin George')
print('o---')
print(' ||||')
print('*' * 10)
## Example 1 just assign variables for a new patient called as john smith - 20 yrs old
## And is a new patient - Try storing the various variables in the given statement
full_name = 'John smith'
age = 20
is_new = True ## True or False boolean values and is case sensitive
## Example 2 get the user input and type a hi message
name = input('What is your name? ')
fav_color = input('what is your favorite color? ')
print(name + " Likes "+ fav_color)
## Type Coversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year) ## Here the age is converted to integer type
print(age)
print(type(age))
