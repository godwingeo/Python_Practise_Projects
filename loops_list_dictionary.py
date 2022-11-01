for items in 'Python':
    print(items)

for item in ['Godwin', 'Sarah', 'Gisha']:
    print(item)

for i in range(10):
    print(i)

for j in range(5, 10): ## here numbers from 5 to (10 - 1) will be printed
    print(j)

for k in range(10, 15, 2): ## here numbers from 5 to (10 - 15) will be printed with step of 2
    print(k)

## find total in the price list
prices = [10, 20 , 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

## Nested Loop mainly to print (X, Y)
## for each values of x corresponding values in y
for x in range(4):
    for y in range(3):
         print(f'({x}, {y})')


## Printing letter F using  list [5, 2, 5, 2, 2]
my_list = [5, 2, 5, 2, 2]
for item in my_list:
    print('*' * item)
## using nested For loop
for each_num in my_list:
    output = ''
    for count in range(each_num):
        output = output + 'x'
    print(output)
names = ['Godwin', 'Sarah', 'Gisha', 'George', "Merly"]
print(names[2:])
print(names[:])  ## using [] does not modify the list it just returns the copy

## modifying the list values
names[0] = 'Johnii' ## the list item gets modified
print(names)
## Write a Program to find the largest number in the list
numbers = [3987654, 6, 2, 8, 3987654, 99, 789, 1092]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)
## List methods
numbers_test = [5, 2, 1, 7, 4]
numbers_test.append(23) ## Add number to the end of the list
print(numbers_test)

## Remove items from list
numbers_test.remove(1)
print(numbers_test)

## Insert item at a particular location or index
numbers_test.insert(1, 29)
print(numbers_test)

## Clear the list
numbers_test.clear() ## No arguments it removes all the items in the list
print(numbers_test)
## pop method gets the last element from list and removes it from the list
numbers_test = [5, 2, 1, 7, 4]
print(numbers_test.pop())
print(numbers_test.pop())
print(numbers_test.pop())
print(numbers_test)
## index of particular item
print(numbers_test.index(2))

## In method
print(5 in numbers_test) ## Returns a boolean value
## count(), sort() , reverse()
numbers = [5, 2, 1, 5, 7, 4]
numbers.sort() ## sort the list in asecending order small to big
numbers.reverse() ## sort the list descending order
print(numbers.count(5)) ## count no of occurence of a particular number

number_02 = numbers.copy() ## .copy method creates a copy of the previous list

## Remove Duplicates from the list
## Creeate another empty list and add the numbers from list 1 as unique values

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques: ##
        uniques.append(number)
print(uniques)
## Tuples
## Tuples are almost like list but one difference is we cannot modify values defined inside
## of a tuple
test_num = (1, 2, 3)
print(test_num)
print(test_num[0])

## unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)
print(y)
print(z)

## entering Phone numbers in digits and it should return the wordings of number

phone = input('Phone: ')
digits_mapping = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

### emoji converter code:

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔"
}
output = ""
for word in words:
    ## here .get method has a word which you entered gets defaulted to same word entered by the user
    output += emojis.get(word, word) + " "
print(output)