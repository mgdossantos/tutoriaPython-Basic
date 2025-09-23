tarefas = []

#criar uma lista de tarefas
tarefas = ["corrigir exercicios", "preparar aula", "lavar roupa"]
#mostrar a lista completa
print(tarefas)

#acessar elementos da lista
print(tarefas[0])
print(tarefas[-1])

#modificar elementos
tarefas[0]="corrigir codigos"
print(tarefas)

#adicionar
#append
tarefas.append("ir ao mercado")
print(tarefas)

#insert
tarefas.insert(1,"lavar o banheiro")
print(tarefas)

#remover
#remove
tarefas.remove("corrigir codigos")
print(tarefas)
#del
del tarefas[2]
print(tarefas)

#pop
tarefa = tarefas.pop()
print(tarefa)
print(tarefas)