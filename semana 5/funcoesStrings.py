#Exemplos de funções úteis de strings em Python

print("\n--- .split() ---")
frase = "Python é divertido"
print(frase.split())  # ['Python', 'é', 'divertido']

texto = "maçã,banana,uva"
print(texto.split(","))  # ['maçã', 'banana', 'uva']

print("\n--- .join() ---")
frutas = ["maçã", "banana", "uva"]
print(" - ".join(frutas))  # maçã - banana - uva

print("\n--- .replace() ---")
mensagem = "Python é difícil"
print(mensagem.replace("difícil", "divertido"))  # Python é divertido

print("\n--- .lower() ---")
nome = "MARCEla"
print(nome.lower())  # marcela

print("\n--- .title() ---")
nome_completo = "marcela dos santos"
print(nome_completo.title())  # Marcela Dos Santos