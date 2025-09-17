
#menu
print("### Menu ###")
print("1 - Gasolina")
print("2 - Diesel")

#entrada de dados
combustivel = input("Opcao: ")
litros = float(input("Digite a quantidade de litros: "))


#processamento
if combustivel == "2":
    preco_litro = 2.00
    if litros <= 25:
        desconto = 0.05
    else:
        desconto = 0.075
elif combustivel == "1":
    preco_litro = 3.00
    if litros <= 25:
        desconto = 0.07
    else:
        desconto = 0.09
else:
    print("Tipo de combustível inválido.")
    exit()

valor_bruto = preco_litro * litros
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

#saida
print(f"Valor a ser pago: R$ {valor_final:.2f}")