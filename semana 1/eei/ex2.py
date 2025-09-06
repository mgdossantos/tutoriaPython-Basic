
#Peça ao usuário um número inteiro e mostre se ele é par ou ímpar (use operadores
#matemáticos e relacionais).

numero = int(input("Digite o numero para testar: "))
#operador para me dar o resultado inteiro da divisao
divisao = numero //2
#operador par ter o resto da divisao
resto = numero % 2

#operador ternario para ter a mensagem Par ou Impar de acordo com o valor armazenado na variavel resto
# == teste para ver se as variaveis sao iguais
# != teste para ver se as variaveis sao diferentes
resultadoParImpar = "Par" if resto == 0 else "Impar"

print("Divisao: ", divisao)
print("Resto: ", resto)
print("Par ou Impar?: ", resultadoParImpar)