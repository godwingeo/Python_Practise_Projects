def greet_user(firstname, lastname):
    print(f'Hi {firstname} {lastname}')
    print('Welcome aboard')


print('Start')
greet_user("Godwin", "George")  ## Function call
print('Finish')

def square(number):
    return number * number;

square = square(3)
print(square)

def emoji_converter_func(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😔"
    }
    output = ""
    for word in words:
        ## here .get method has a word which you entered gets defaulted to same word entered by the user
        output += emojis.get(word, word) + " "
    return output

messag = input(">")

covereted_text = emoji_converter_func(messag)
print(covereted_text)

## exception handling
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Please enter Valid Integer as Age")
except ZeroDivisionError:
    print("Age cannot be 0.")