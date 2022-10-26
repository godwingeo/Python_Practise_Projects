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
## Strings
course = 'Python for beginners' ### Python
         #012345 ---index for word Python
print(course[0]) ## Note - Indexing starts from ZERO
print(course[1])
print(course[-1]) ## Last letter from the end.
print(course[-2]) ## Second Last letter from the end
## Printing certain range of characters
print(course[0:3]) ## Starts from zero but ends at n-1 i.e 3-1 = 2, Index 3 is excluded

## Having only the start index in the square brackets
print(course[0:]) ## copy of string ## here end index is assumed as length of the string
print(course[1:]) ## ignores letter P alone and prints remaining --- ython for beginners
print(course[:5]) ## so here start index is assumed as 0 by python i.e 0 to n-1 (4) is returned
## Here 0 will be assumed as start index and length of string as the end index
## This will create a copy of the entire string
print(course[:])
another = course[:]
print('The copy is ')
print(another)
## Find the output
name = 'Jennifer'
## starts with index 1 = e , and ends at e , since -1 = r , a letter before r i.e- e
print(name[1:-1]) ## o/p - ennife

## Fromatted string
## It helps to visualize the output in a better way
first = 'John'
last = 'Smith'
## we need a message as john [smith] is a coder
message = first + ' [' + last + '] is a coder'
print(message)
## formatted string conversion here f means formated string {} has variable in it
msg = f'{first} [{last}] is a coder'
print(msg)