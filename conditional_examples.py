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