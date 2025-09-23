tarefas = {
    "tarefa1": "pendente",
    "tarefa2": "em andamento",
    "tarefa3": "concluída"
}

print(tarefas)

print(tarefas["tarefa1"])   # mostra 'pendente'
print(tarefas.get("tarefa3"))  # outra forma -> 'concluída'

tarefas["tarefa1"] = "concluída"
print(tarefas)

tarefas["tarefa4"] = "pendente"
print(tarefas)

del tarefas["tarefa2"]
print(tarefas)