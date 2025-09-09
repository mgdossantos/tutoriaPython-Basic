soma = 0
while True:
    valor = input("Digite um numero ou sair:")
    if valor.lower()=="sair":
        break
    soma= soma + float(valor)
print("Soma: ", soma)