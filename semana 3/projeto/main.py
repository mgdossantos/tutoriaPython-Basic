# Variáveis para armazenar tarefas (iniciando como vazias ou com um valor padrão)
tarefa1 = None
tarefa1Status=None
tarefa2 = None
tarefa2Status=None
tarefa3 = None
tarefa3Status= None
contadorTarefas=0

#Criar um loop para manter o menu ativo até que a pessoa escolha "sair".
#Possibilidade de repetir a adição de tarefas.
print("===================================")
print(" Bem-vindo ao Gerenciador de Tarefas ")
print("===================================\n")

print("Escolha uma opção:")
print("1 - Ver tarefas")
print("2 - Adicionar tarefa")
print("3 - Sair")

# .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
# facilitando a verificação das opções.
opcao = input("Digite o número da opção desejada: ").strip()

while(opcao!="3"):
    if opcao == "1":
        print("\n--- Suas Tarefas ---")
        "Verificar se existe tarefa para ser mostrada"
        if tarefa1:
            print("1." , tarefa1)
        if tarefa2:
            print("2." , tarefa2)
        if tarefa3:
            print("3." , tarefa3)
        if not tarefa1 and not tarefa2 and not tarefa3:
            print("Nenhuma tarefa adicionada ainda.")
        print("--------------------\n")
    elif opcao == "2":
        if contadorTarefas < 3:
            nova_tarefa = input("Digite a nova tarefa: ").strip()
            if contadorTarefas == 0:
                tarefa1 = nova_tarefa
            elif contadorTarefas == 1:
                tarefa2 = nova_tarefa
            elif contadorTarefas == 2:
                tarefa3 = nova_tarefa
            contadorTarefas += 1
            print("Tarefa adicionada com sucesso!\n")
        else:
            print("\nVocê já adicionou o número máximo de tarefas (3). Remova uma para adicionar outra.\n")
    else:
        print("\nOpção inválida. Tente novamente.\n")

    print("===================================")
    print(" Bem-vindo ao Gerenciador de Tarefas ")
    print("===================================\n")

    print("Escolha uma opção:")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Sair")

    # .strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
    # facilitando a verificação das opções.
    opcao = input("Digite o número da opção desejada: ").strip()

print("\nSaindo do programa. Até logo!")
