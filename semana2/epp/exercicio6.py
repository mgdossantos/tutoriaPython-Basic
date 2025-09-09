'''
Spathiphyllum, mais comumente conhecido como lírio da paz ou
planta de vela branca, é uma das plantas de interior mais populares que
filtra as toxinas nocivas do ar. Algumas das toxinas que neutraliza
incluem benzeno, formaldeído e amônia.

Imagine que seu programa de computador adora essas plantas. Sempre
que recebe uma entrada na forma da palavra Spathiphyllum,
involuntariamente grita para o console a seguinte string:
"Spathiphyllum é a melhor planta de todas!"
'''

planta = input("Digite o nome de uma planta: ")

if planta == "Spathiphyllum":
    print("Spathiphyllum eh a melhor de todas!!")
elif planta == "spathiphyllum":
    print("Nao, eu quero Spathiphyllum Grande!")
else:
    print("Spathiphyllum!!!Nao quero", planta)