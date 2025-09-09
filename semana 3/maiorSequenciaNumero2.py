maior = float('-inf')  # começa com o menor número possível

while True:
    numero = input("Digite um numero ou 'sair': ")

    if numero.lower() == 'sair':
        break  # Encerra o laço caso o usuário digite 'sair'

    if not numero:  # Caso o usuário só aperte ENTER
        continue  # Volta para o início do laço sem fazer nada

    try:
        valor = float(numero)
        if valor > maior:
            maior = valor
    except ValueError:
        print("Digite apenas números ou 'sair'!")
        continue  # Se não for número, volta para o início do laço

print("Maior numero: ", maior)