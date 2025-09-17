#Agora seu programa precisa receber a idade e dizer se o usuário é
#menor de 18 anos, maior e quando ele tem 18 anos.

idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de 18 anos!")
elif idade == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você é maior de 18 anos!")