#que ela seja global
livros=[] #cada elemento {"titulo":str, "valor": float}

#criar uma funcao que peca o livro e adicione a lista
def inserirLivro():
    titulo=input("Digite o titulo: ")
    valor = float(input("Digite o valor: "))
    livros.append({"titulo":titulo,"valor":valor})

#criar uma funcao que mostre todos os livros da lista
def mostrarLivros():
    # for a in livros:
    #     print("Titulo: ", a)
    #indice + valor
    for i,livro in enumerate(livros):
        print("Indice: ",i,"-- Titulo: ",livro["titulo"], "Valor: ", livro["valor"])

#criar um menu para escolher operacao
def menu():
    print("-- Menu --")
    print("1 - Inserir livro")
    print("2 - Mostrar livros cadastrados")
    print("3 - Deletar pelo titulo")
    print("4 - Procurar pelo titulo")
    print("5 - Procurar pelo indice")
    print("6 - Sair")

while True:
    menu()
    op= input("Digite uma opcao: ")
    if op=="6":
        break
    elif op=="1":
        inserirLivro()
    elif op=="2":
        mostrarLivros()
    else:
        print("Opcao Invalida")


















#criar o programa principal
# inserirLivro()
# print(livros)
# inserirLivro()
# print(livros)

# inserirLivro()
# mostrarLivros()
# inserirLivro()
# mostrarLivros()
