tarefas=[]

def inserirTarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)

def mostrarTarefas():
   for t in tarefas:
       print("Task: ", t)

def menu():
    print("Menu")
    print("1 - Inserir Tarefa")
    print("2 - Mostrar Tarefa")
    print("3 - Sair")

while True:
    menu()
    op = int(input("Escolha uma opcao: "))
    if op==1:
        inserirTarefa()
    elif op==2:
        mostrarTarefas()
    elif op==3:
        break
