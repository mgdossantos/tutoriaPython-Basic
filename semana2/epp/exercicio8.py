respostas_positivas = 0

resposta = input("Você ligou para a vítima? (sim /não): ").strip().lower()
if resposta == "sim":
    respostas_positivas = respostas_positivas +1

resposta = input("Você estava na cena do crime? (sim/não): ").strip().lower()
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Você mora perto da vítima? (sim/não): ").strip().lower()
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Devia à vítima? (sim/não): ").strip().lower()
if resposta == "sim":
    respostas_positivas += 1

resposta = input("Você já trabalhou com a vítima? (sim/não): ").strip().lower()
if resposta == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Classificação: Suspeito")
#quando meu teste for verdadeiro
# or: op1 or op2
# para que o resultado do or seja verdadeiro
# eu preciso de no minimo um dos dois verdadeiro
#elif 3<= respostas_positivas <= 4
elif respostas_positivas==3 or respostas_positivas==4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")