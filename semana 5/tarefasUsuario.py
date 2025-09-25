tarefas=[]

def inserirTarefa():
    tarefa=input("Digite a tarefa: ")
    tarefas.append(tarefa)
def mostrarTarefas():
    for a in tarefas:
        print("Tarefa: ",a)

def menu():
    print("Menu")
    print("1 - Inserir Tarefa")
    print("2 - Mostrar Tarefas")



while True:
    menu()
    op=int(input("Digite uma opcao: "))
    if op==1:
        inserirTarefa()
    elif op==2:
        mostrarTarefas()
    elif op ==3:
        break
    else:
        print("Valor invalido")
