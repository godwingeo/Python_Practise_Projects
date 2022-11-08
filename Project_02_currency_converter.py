
from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://free.currconv.com/"
API_KEY = "9a7058e7b2c6c6dfde7a"

printer = PrettyPrinter() ## Helps to format the JSON file

## Function to get the list of currencies available from the API realtime
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data
data = get_currencies()

## Function to print the currencies in a proper format
def print_currencies(currencies):
    for name, currency in currencies: ## This isteration is tuple iteration
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', "")
        print(f"{_id} - {name} - {symbol}")

## Function to get the exchange rate between the currencies
def exchange_rate(currency1, currency2):
    endpoint = f'api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()
    if len(data) == 0:
        print('Invalid currencies')
        return
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate
## Find the Total Amount in coverted Format using Formula: converted_amount = rate * amount
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid Amount.")
        return
    converted_amount = rate * amount
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount

## Main function to get the inputs from the user and generate the results using above functions
def main():
    currencies = get_currencies()
    print("Welcome to currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = float(input(f"Enter an amount in {currency1}: "))
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command")

main()