import operacoesModulo, entradaSaida

primeiroNumero = entradaSaida.pedirNumero()
segundoNumero = entradaSaida.pedirNumero()

soma = operacoesModulo.soma(primeiroNumero, segundoNumero)
entradaSaida.saida(soma)