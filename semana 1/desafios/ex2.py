#Crie um mini-simulador de compras: o programa deve perguntar o preço de dois produtos e
# exibir o valor total e o desconto de 10% aplicado.

produto1 = float(input("Digite o valor do produto 1: "))
produto2 = float(input("Digite o valor do produto 2: "))

total = produto1+produto2
desconto = 0.1*total

print("Total: R$ ",total)
print("Desconto a ser aplicado: R$ ",desconto)