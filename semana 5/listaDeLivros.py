# Criar uma lista com 5 livros e imprimir com numeração.

#criar
livros=["elza soares biografia", "mulheres que correm com os lobos", "1984", "senhor dos aneis", "robot"]
print("**Antes**")
print(livros)

#acessar elementos
# print(livros[0])
# print(livros[1])
# print(livros[2])
# print(livros[-1])
livroEscolhido = livros[-1]

#modificar
livros[1]="apartamento em paris"
print("**Depois de modificar**")
print(livros)

#adicionar
livros.append("a empregada")
print("**Depois de adicionar**")
print(livros)

#insert (onde, oque)
livros.insert(2,"jantar secreto")
print("**Depois de inserir**")
print(livros)

#remover
#remove : pelo elemento
livros.remove("apartamento em paris")
print("**Depois de remover**")
print(livros)

del livros[4]
print("**Depois de deletar**")
print(livros)

#tamanho da lista
tamanho = len(livros)
print("Tamanho da lista: ", tamanho)

#pop
livro = livros.pop()
print("O retorno de pop: ", livro)
