#entrada
#peco as info para calcular e mostrar o solicitado
nome= input("Digite o nome do funcionario: ")
salarioBruto = float(input("Digite o salario bruto: "))
impostos =  float(input("Digite o valor em impostos (%): "))

#processamento
#calculo o desconto e armazeno no desconto
#subtraio do bruto e armazeno no liquido
desconto = (impostos/100*salarioBruto)
salarioLiquido = salarioBruto - desconto

#saida
#mostro o nome e o salario liquido de cada funcionario
print("Nome: ",nome)
print("Salario Liquido: R$",salarioLiquido)
