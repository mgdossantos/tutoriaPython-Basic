#Crie um programa que pergunte o ano de nascimento do usuário e calcule a idade atual.
# Em seguida, mostre uma mensagem dizendo se ele é maior ou menor de idade.

nome = input("Digite seu nome: ")
anoNascimento = int(input("Digite o ano de nascimento: "))
idadeAtual = 2025 -anoNascimento
resultado = "maior e igual de idade" if idadeAtual > 18 else "menor de idade"
print(nome, "voce eh", resultado,".")