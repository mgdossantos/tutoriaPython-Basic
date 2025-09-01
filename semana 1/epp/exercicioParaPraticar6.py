#Peça duas variaveis numericas para o usuario e exiba:
# Soma, subtração, multiplicação e divisão
# maior, menor, igual e diferente
#Realize as operacoes do primeiro numero com o segundo


numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

soma = numero1 +numero2
subtracao = numero1 - numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

print("Soma: ",soma)
print("Subtracao: ",subtracao)
print("Multiplicacao: ",multiplicacao)
print("Divisao: ", divisao)


maior = numero1 > numero2
print("Numero 1 eh maior que numero 2? ", maior)
menor = numero1 < numero2
print("Numero 1 eh menor que numero 2? ", menor)
igual = numero1 == numero2
print("Numero 1 eh a igual a numero 2? ", igual)
diferente = numero1 !=numero2
print("Numero 1 eh igual a numero 2? ", diferente)



