#que ela seja global
livros=[]

#criar uma funcao que peca o livro e adicione a lista
def inserirLivro():
    livro=input("Digite o titulo: ")
    livros.append(livro)

#criar uma funcao que mostre todos os livros da lista
def mostrarLivros():
    for a in livros:
        print("Titulo: ", a)

#criar um menu para escolher operacao
def menu():
    print("-- Menu --")
    print("1 - Inserir livro")
    print("2 - Mostrar livros cadastrados")
    print("3 - Deletar pelo titulo")
    print("4 - Procurar pelo titulo")
    print("5 - Sair")

while True:
    menu()
    op= input("Digite uma opcao: ")
    if op=="5":
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
