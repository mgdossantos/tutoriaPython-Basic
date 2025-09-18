
numero = input("Digite um numero ou sair: ")

#estabelecer a palavra sair para parar
# criar o menor numero possivel para ser substituido pelo primeiro numero digitado
maior = float('-inf')  # começa com o menor número possível


while numero.lower() != 'sair':

    if float(numero) > maior:
        maior = float(numero)

    numero = input("Digite um numero ou sair: ")

print("Maior numero: ", maior)