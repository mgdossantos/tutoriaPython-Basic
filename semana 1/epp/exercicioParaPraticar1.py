#Crie um algoritmo para fazer conversao de Real para CAD
import requests

def get_brl_to_cad():
    url = 'https://economia.awesomeapi.com.br/json/last/BRL-CAD'
    response = requests.get(url)
    data = response.json()
    # O valor de compra está em 'bid'
    brl_cad = float(data['BRLCAD']['bid'])
    return brl_cad

#Esse codigo traz a taxa usando uma API
# real = float(input("Digite o valor a ser convertido:R$ "))
# tax = get_brl_to_cad()
# cad = real*tax
#
# print("Valor em CAD: ",cad)

#Esse codigo coloca o codigo em hardcode

real = float(input("Digite o valor a ser convertido:R$ "))
tax = 0.253
cad = real*tax

print("Valor em CAD: ",cad)