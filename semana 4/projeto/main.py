#Transformar comandos repetidos em funções (ex: mostrar menu, adicionar tarefa, listar tarefas).
#Separar o código principal e funções auxiliares.

# Variáveis para armazenar tarefas (iniciando como vazias ou com um valor padrão)
tarefa1 = None
tarefa1Status=None
tarefa2 = None
tarefa2Status=None
tarefa3 = None
tarefa3Status= None
contadorTarefas=0

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

mostrar_menu()
# .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
# facilitando a verificação das opções.
opcao = input("Digite o número da opção desejada: ").strip()

while(opcao!="3"):
    if opcao == "1":
        ver_tarefas()

    elif opcao == "2":
        if contadorTarefas < 3:
            num_tarefa_para_adicionar = int(input("Qual número de tarefa deseja adicionar (ex: 1, 2, 3)? ").strip())
            nova_tarefa = input("Digite a nova tarefa: ").strip()
            adicionar_tarefa(num_tarefa_para_adicionar, nova_tarefa)
        else:
            print("\nVocê já adicionou o número máximo de tarefas (3). Remova uma para adicionar outra.\n")
    else:
        print("\nOpção inválida. Tente novamente.\n")

    mostrar_menu()

    # .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
    # facilitando a verificação das opções.
    opcao = input("Digite o número da opção desejada: ").strip()

print("\nSaindo do programa. Até logo!")
