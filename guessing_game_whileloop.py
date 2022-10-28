i = 1 ## Intalization
while i <= 5: ## condition to consider to break the loop
    print(i)
    i = i + 1 ## incrementing
print('Done')

## Program to print **
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')
## Guessing Game ## setting up
secret_num = 9 ## secret number set inside the program
guess_count = 0 # this is like i
guess_limit = 3 # Allowing user to count 3 times
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_num:
        print('You won!')
        break
else:   ### In python the while loop can have an else part
    print('You have Failed.Better luck next time !')