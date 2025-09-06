#Implementar um menu com 2 opções no programa.

primeiro = float(input("Primeiro numero:"))
segundo = float(input("Segundo numero:"))

print("** Menu **")
print("1 - Soma")
print("2 - Subtracao")

op = input("Escolha uma operacao: ")

if op =="1":
    resultado = primeiro+segundo
elif op=="2":
    resultado = primeiro - segundo


print("Resultado: ", resultado)