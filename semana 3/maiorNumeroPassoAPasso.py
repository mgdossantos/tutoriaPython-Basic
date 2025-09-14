

numero = input("Digite o numero ou sair: ")
maior = 0

while numero!="sair":
    #verificar se eh o maior
    numeroConvertido = int(numero)
    if  numeroConvertido> maior:
        maior=numeroConvertido

    numero = input("Digite o numero ou sair: ")
print("Maior numero digitado: ",maior)