# Create an algorithm to convert Brazilian Real (BRL) to Canadian Dollar (CAD)
import requests

def get_brl_to_cad():
    url = 'https://economia.awesomeapi.com.br/json/last/BRL-CAD'
    response = requests.get(url)
    data = response.json()
    # The purchase value is stored in 'bid'
    brl_cad = float(data['BRLCAD']['bid'])
    return brl_cad

# This code retrieves the exchange rate using an API
real = float(input("Enter the amount to be converted (BRL): R$ "))
tax = get_brl_to_cad()
cad = real * tax

print("Value in CAD: ", cad)

# ---------------------------------------------------
# Alternative: Hardcoded exchange rate (without API)
# ---------------------------------------------------
# real = float(input("Enter the amount to be converted (BRL): R$ "))
# tax = 0.253
# cad = real * tax
# print("Value in CAD: ", cad)