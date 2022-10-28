is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear a warm clothes")
else:
    print("its a lovely day")
print("Enjoy your Day")

## exercise  Price of a house is $1M - if buy has a good credit
## put 10% otherwise---- Note: Million means 10 lakhs

price = 1000000
has_good_credit = False
if has_good_credit:
    downpayment = price * 0.1
else:
    downpayment = price * 0.2
print(f"Downpayment:${downpayment}")

## Logical operators
## if applicant has high income And good credit then eligible for loan
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:  ## We can also change And operator to or operator
    print("Eligible for loan")
## NOT operator
## If applicatant has good credit and Not having any criminal record then eligible for loan
## NOTE- and, or , not all in small letters
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# comparison operators: <, >, <=, >= , Equality operator == , !=,
## Note - eg - a = 5 -- Here equal to sign is a assignment operator, where as == is equality operator
