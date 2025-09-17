
#Criação do esqueleto inicial do gerenciador de tarefas (arquivo .py, estrutura geral).
# Interface simples no terminal: primeira mensagem de boas-vindas no programa.

print("===================================")
print(" Bem-vindo ao Gerenciador de Tarefas ")
print("===================================\n")

print("Escolha uma opção:")
print("1 - Ver tarefas")
print("2 - Adicionar tarefa")
print("3 - Sair")

#.strip() serve para garantir que a entrada do usuário não tenha espaços extras antes ou depois,
# facilitando a verificação das opções.
opcao = input("Digite o número da opção desejada: ").strip()

if opcao == "1":
    print("\n[Funcionalidade de ver tarefas ainda não implementada]\n")
elif opcao == "2":
    print("\n[Funcionalidade de adicionar tarefa ainda não implementada]\n")
elif opcao == "3":
    print("\nSaindo do programa. Até logo!")
else:
    print("\nOpção inválida. Tente novamente.\n")

