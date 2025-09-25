def pedirNumero():
    "Funcao responsavel por solicitar o numero e retorna ele convertido em float"
    return float(input("Digite um numero: "))

def saida(resultado):
    print("Resultado: ",str(resultado))

def menu():
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Sair")