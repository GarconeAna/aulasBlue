#### Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma 
# desses três argumentos.

def somar(n1,n2,n3) :
    somados = n1 + n2 + n3
    return somados

num1 = int(input('Qual é o primeiro número? '))
num2 = int(input('Qual é o segundo número? '))
num3 = int(input('Qual é o terceiro número? '))
print(somar(num1,num2,num3))


#### Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de 
# caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def verificando(num) :
    if num > 0 :
        return 'P'
    elif num < 0 :
        return 'N'
    elif num == 0 :
        return '0'

numero = int(input('Digite um numero: '))
print(verificando(numero))


#### Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros 
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
# custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo 
# para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo) :
    t = taxaImposto/100
    imposto = t * custo 
    impostoIncluso = imposto + custo
    return impostoIncluso

custoProduto = float(input('Qual valor do produto? '))
taxaNoCusto = float(input('Qual porcentagem da taxa? '))
print(somaImposto(taxaNoCusto,custoProduto))

#### Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional
#  de 1.5 nas horas extras trabalhadas.




#### Faça um programa que calcule através de uma função
#  o IMC de uma pessoa que tenha 1,68 e pese 75kg.

def imc() :
    calculo = 75 / (1.68**2)
    return calculo

print(imc())

# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota	Conceito
# >=9.0	A
# >=8.0	B
# >=7.0	C
# >=6.0	D
# <=4.0	F






# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.

def verificar(n1,n2) :
    if n1 > n2 :
        return f'{n1} é maior.'
    elif n2 > n1 :
        return f'{n2} é maior'
    else :
        return 'Os números são iguais.'

num1 = int(input('Qual número da vez? '))
num2 = int(input('Qual é o outro número? '))
print(verificar(num1,num2))


# DESAFIO Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e 
# retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos 
# temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

