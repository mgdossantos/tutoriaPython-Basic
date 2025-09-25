import operacoesModulo,entradaSaida


#resultado= operacoesModulo.soma(3,5)
#print(resultado)

while True:


    entradaSaida.menu()

    op =int( input("Escolha uma opcao: "))

    if op!=3:

        numero1=entradaSaida.pedirNumero()
        numero2=entradaSaida.pedirNumero()
        if op == 1:
            resultado = operacoesModulo.soma(numero1,numero2)
            entradaSaida.saida(resultado)
        elif op ==2:
            resultado = operacoesModulo.subtracao(numero1, numero2)
            entradaSaida.saida(resultado)
    else:
        break
