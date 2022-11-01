from requests import get
from pprint import PrettyPrinter
##BASE_URL = "https://free.currconv.com/"
## API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter() ## Helps to format the JSON file


json = {'results': {'AED': {'currencyName': 'UAE Dirham', 'id': 'AED'},
             'AFN': {'currencyName': 'Afghan Afghani', 'id': 'AFN', 'currencySymbol': '^'},
             'USA': {'currencyName': 'US dollar', 'id': 'USD', 'currencySymbol': '$'},
             'INR': {'currencyName': 'Indian Rupee', 'id': 'INR', 'currencySymbol': 'RS'},
             'CAD': {'currencyName': 'Canadian Dollars', 'id': 'CAD', 'currencySymbol': '$'}
             }
 }
json_exchange_rate = {
    'AED_INR': 22.50,
    'USD_INR': 82.66,
    'CAD_INR': 60.99,
    'AFN_INR': 0.93

}

def get_currencies():
    ##endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    ##url = BASE_URL + endpoint
    ##printer.pprint(data)
    data = json['results'] ## This will get the exact dictionary of results
    data = list(data.items()) ## coverting the Dictionary to a List so that we can sort the currency
    data.sort()
    print(type(data))
    return data

def print_currencies(currencies):
    for name, currency in currencies: ## This isteration is tuple iteration
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', "")
        print(f"{_id} - {name} - {symbol}")
my_data = get_currencies()
##printer.pprint(my_data)
print_currencies(my_data)

def exchange_rate(currency1, currency2):
    ky = str(currency1 +"_"+ currency2 )
    data = json_exchange_rate[ky]  ## Normally from API this have a LIST conversion
    rate = data
    print(f"{currency1} -> {currency2} = {rate}")
    return rate

exchange_rate('USD', 'INR')

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    converted_amount = rate * amount
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount


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