import sys
import requests

def main():

    # Block of code to check if the argument passed meets all the requirements.
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        sys.exit("You supposed to pass two arguments!")
    else:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Command line argument is not a number!")

    # Finally converting the argeument through get_price() and printing out the results.
    print(f"${get_price(amount):,.4f}")


def get_price(amount):

    # Collecting the live bitcoin price in Usd($) from the Coincap website and assigning it a variable.
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=d9148d47004e04071e32c22150e017da5aaac69f212afe17c2c375931255bf88"
    bitcoin = requests.get(url)
    current = bitcoin.json()
    price = current["data"]["priceUsd"]

    # Calculating the price of bitcoin for a buyer.
    return(float(price) * amount)




main()