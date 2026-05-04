
"""
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be
converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey
with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the
current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
"""
import json
import sys
import requests
api_key="fuck_you"
if len(sys.argv)==2:
    try:
        Quantity=float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")
except requests.RequestException:
    pass
data=response.json()
Amount= float(data["data"]["priceUsd"])
Amount=Amount*Quantity
Amount=round(Amount, 4)

print(f"${Amount:,.4f}")
