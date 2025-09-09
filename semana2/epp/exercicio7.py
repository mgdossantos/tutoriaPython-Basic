combustivel = input("Digite o tipo de combustível (gasolina/diesel): ").lower()
litros = float(input("Digite a quantidade de litros: "))

if combustivel == "diesel":
    preco_litro = 2.00
    if litros <= 25:
        desconto = 0.05
    else:
        desconto = 0.075
elif combustivel == "gasolina":
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

print(f"Valor a ser pago: R$ {valor_final:.2f}")