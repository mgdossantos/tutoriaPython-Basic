tarefas = []  # cada elemento será {"titulo": str, "status": str}

def inserirTarefa():
    titulo = input("Digite a tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "status": "pendente"})
    else:
        print("Título não pode ser vazio.")

def mostrarTarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    # enumerate: índice + valor
    for i, t in enumerate(tarefas):
        print(i, "-", t["titulo"], "| Status:", t["status"])

def ler_indice(mensagem):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return None
    mostrarTarefas()
    entrada = input(mensagem).strip()
    if not entrada.isdigit():
        print("Você deve digitar um número inteiro não negativo.")
        return None
    idx = int(entrada)
    if idx < 0 or idx >= len(tarefas):
        print("Índice fora do intervalo válido.")
        return None
    return idx

def concluirTarefa():
    idx = ler_indice("Digite o índice da tarefa para concluir: ")
    if idx is not None:
        tarefas[idx]["status"] = "concluída"
        print("Tarefa concluída!")

def removerTarefa():
    idx = ler_indice("Índice para remover: ")
    if idx is not None:
        del tarefas[idx]
        print("Tarefa removida!")

def editarTarefa():
    idx = ler_indice("Índice para editar: ")
    if idx is not None:
        novo_titulo = input("Novo título: ").strip()
        if novo_titulo:
            tarefas[idx]["titulo"] = novo_titulo
            print("Tarefa editada!")
        else:
            print("Título não pode ser vazio.")

def menu():
    print("\nMenu")
    print("1 - Inserir Tarefa")
    print("2 - Mostrar Tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Editar Tarefa")
    print("5 - Remover Tarefa")
    print("6 - Sair")

while True:
    menu()
    op = input("Escolha uma opção: ").strip()
    if op == "1":
        inserirTarefa()
    elif op == "2":
        mostrarTarefas()
    elif op == "3":
        concluirTarefa()
    elif op == "4":
        editarTarefa()
    elif op == "5":
        removerTarefa()
    elif op == "6":
        break
    else:
        print("Opção inválida.")
