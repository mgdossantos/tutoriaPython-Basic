def mostrar_menu():
    print("===================================")
    print(" Bem-vindo ao Gerenciador de Tarefas ")
    print("===================================\n")
    print("Escolha uma opção:")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Sair")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista de tarefas (sem limite de quantidade)."""
    descricao = input("Digite a nova tarefa: ").strip()
    tarefa = {"descricao": descricao, "status": "pendente"}
    tarefas.append(tarefa)
    print(f"Tarefa adicionada: {descricao}")

def ver_tarefas(tarefas):
    """Exibe as tarefas armazenadas na lista."""
    print("\n--- Suas Tarefas ---")
    if tarefas:
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa['descricao']} - Status: {tarefa['status']}")
    else:
        print("Nenhuma tarefa adicionada ainda.")
    print("--------------------\n")

def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída pelo número."""
    if not tarefas:
        print("Nenhuma tarefa para concluir.\n")
        return
    ver_tarefas(tarefas)
    try:
        num = int(input("Digite o número da tarefa que deseja concluir: "))
        if 1 <= num <= len(tarefas):
            if tarefas[num-1]["status"] == "concluída":
                print("Esta tarefa já está concluída.\n")
            else:
                tarefas[num-1]["status"] = "concluída"
                print(f"Tarefa '{tarefas[num-1]['descricao']}' marcada como concluída!\n")
        else:
            print("Número de tarefa inválido.\n")
    except ValueError:
        print("Por favor, digite um número válido.\n")