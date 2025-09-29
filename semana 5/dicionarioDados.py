#Criar um dicionário com dados de uma pessoa e imprimir uma frase personalizada.
registroAluna={
    "nome":"Lais Souza",
    "idade": 33,
    "nacionalidade":"Brasileira"
}

print(registroAluna["nome"],"tem ", registroAluna["idade"], " anos e eh ", registroAluna["nacionalidade"])
print(registroAluna.get("nome"))
print(registroAluna.get("sobrenome","sem info"))
print(registroAluna.keys())
print(registroAluna.values())
print(registroAluna.items())