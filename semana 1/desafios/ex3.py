#Desenvolva um programa que pergunte ao usuário três palavras diferentes e as imprima em
#ordem alfabética.

palavra1=input("Palavra 1: ")
palavra2=input("Palavra 2: ")
palavra3=input("Palavra 3: ")

ordenadas = sorted([palavra1,palavra2,palavra3])
print("Palavras em ordem alfabetica: ", ordenadas)


