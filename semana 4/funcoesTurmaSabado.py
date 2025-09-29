#a funcao
def funcaoOla(user):
    print("Ola ", user," !!")
#Crie um programa que receba um número e retorne P se ele for positivo,
# N se ele for negativo ou zero
def positivoNegativo(numero):
    if numero >0:
        return 'P'
    else:
        return 'N'


#usar a funcao ola
usuario = input("Digite seu nome: ")
funcaoOla(usuario)

#usar a funcao positivoNegativo
print("Positivo ou Negativo? ",positivoNegativo(8))

