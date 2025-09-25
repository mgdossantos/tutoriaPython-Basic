
#criar uma lista de tarefas
tarefas = ["estudar Python","ir ao mercado","tirar o lixo"]
print(tarefas)
print("Tamanho da lista: ",len(tarefas))
#acessar elementos da lista
print(tarefas[0])
print(tarefas[1])
print(tarefas[-1])
#modificar elementos
tarefas[0]="aula de pop-funk"
print("Depois de modificar")
print(tarefas)
#adicionar
#append
tarefas.append("estudar Calculo")
print("Depois de modificar")
print(tarefas)


#insert
#insert(aonde,oq)
tarefas.insert(1,"corrigir provas")
print("Depois de modificar")
print(tarefas)


#remover
#remove
tarefas.remove("estudar Calculo")
print("Depois de modificar")
print(tarefas)

#del
del tarefas[3]
print("Depois de modificar")
print(tarefas)

#pop
tarefa = tarefas.pop()
print(tarefa)
print(tarefas)