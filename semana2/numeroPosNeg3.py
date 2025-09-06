numero = int(input("Digite o numero: "))
#teste
# variavel operador relacional

if numero==0:
    #bloco a ser executado caso o teste seja verdadeiro
    print("Numero igual a zero!")

else:
    # bloco a ser executado caso o teste seja falso
    if numero <0:
        print("Numero negativo!")
    else:
        print("Numero positivo")
print("estou fora do if")