
#Peça ao usuário um número inteiro e mostre se ele é par ou ímpar (use operadores
#matemáticos e relacionais).

numero = int(input("Digite o numero para testar: "))

#
resultado= "Par" if numero%2==0 else "Impar"
print("O numero ",numero, "eh ", resultado)