#Transformar comandos repetidos em funções (ex: mostrar menu, adicionar tarefa, listar tarefas).
#Separar o código principal e funções auxiliares.

# Variáveis para armazenar tarefas (iniciando como vazias ou com um valor padrão)

import utils
tarefa1 = None
tarefa1Status=None
tarefa2 = None
tarefa2Status=None
tarefa3 = None
tarefa3Status= None
contadorTarefas=0



utils.mostrar_menu()
# .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
# facilitando a verificação das opções.
opcao = input("Digite o número da opção desejada: ").strip()

while(opcao!="3"):
    if opcao == "1":
        utils.ver_tarefas()

    elif opcao == "2":
        if contadorTarefas < 3:
            num_tarefa_para_adicionar = int(input("Qual número de tarefa deseja adicionar (ex: 1, 2, 3)? ").strip())
            nova_tarefa = input("Digite a nova tarefa: ").strip()
            utils.adicionar_tarefa(num_tarefa_para_adicionar, nova_tarefa)
        else:
            print("\nVocê já adicionou o número máximo de tarefas (3). Remova uma para adicionar outra.\n")
    else:
        print("\nOpção inválida. Tente novamente.\n")

    utils.mostrar_menu()

    # .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
    # facilitando a verificação das opções.
    opcao = input("Digite o número da opção desejada: ").strip()

print("\nSaindo do programa. Até logo!")
