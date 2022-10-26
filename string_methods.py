course = 'Python for Beginners'
## Use of len function to get the string length even space is counted
print(len(course))
## string related methods example
## upper converts to upper case
print(course.upper())
print(course) ## the  same is retained without any change
## lower method converts to lower case
print(course.lower())
## returns the index of P from the above string and find method is case sensitive
## it will return -1 if the character is not found
print(course.find('P'))
## using the find method on the entire string itself
print(course.find('Beginners')) ## Here o/p will be 11 since letter B index is 11 and
# it will be returned

## replace a particular string eg - Beginners with Absolute Beginners
## o/p will be Python for Absolute Beginners
print(course.replace('Beginners', 'Absolute Beginners'))
## similarly we can use single character
print(course.replace('P', 'J')) ## o/p print(course.replace('P', 'J'))

## Use of IN key word - we can check existence of a string or character
print('Python' in course) ## o/p - True
print('python' in course) ## o/p -False
## in keyword retuns a boolean value where as find  will return index 
