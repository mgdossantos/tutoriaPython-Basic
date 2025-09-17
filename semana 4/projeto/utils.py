def mostrar_menu():
    print("===================================")
    print(" Bem-vindo ao Gerenciador de Tarefas ")
    print("===================================\n")

    print("Escolha uma opção:")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")

def adicionar_tarefa(numero_tarefa, descricao):
    """Adiciona uma tarefa a uma variável específica."""
    print("\n--- Suas Tarefas ---")
    "Verificar se existe tarefa para ser mostrada"
    if numero_tarefa==1:
        global tarefa1
        tarefa1=descricao
        print("1.", tarefa1)
    if numero_tarefa==2:
        global tarefa2
        tarefa2 = descricao
        print("2.", tarefa2)
    if numero_tarefa==3:
        global tarefa3
        tarefa3 = descricao
        print("3.", tarefa3)


def ver_tarefas():
    """Exibe as tarefas armazenadas nas variáveis."""
    print("\n--- Suas Tarefas ---")
    if tarefa1:
        print(f"1. {tarefa1}")
    if tarefa2:
        print(f"2. {tarefa2}")
    if tarefa3:
        print(f"3. {tarefa3}")
    # Adicione mais ifs para exibir as outras tarefas
    if not tarefa1 and not tarefa2 and not tarefa3:
        print("Nenhuma tarefa adicionada ainda.")
    print("--------------------\n")