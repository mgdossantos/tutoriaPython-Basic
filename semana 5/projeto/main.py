import utils

def main():
    tarefas = []
    while True:
        utils.mostrar_menu()
        opcao = input("Digite o número da opção desejada: ").strip()
        if opcao == "1":
            utils.ver_tarefas(tarefas)
        elif opcao == "2":
            utils.adicionar_tarefa(tarefas)
        elif opcao == "3":
            utils.concluir_tarefa(tarefas)
        elif opcao == "4":
            print("\nSaindo do programa. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()