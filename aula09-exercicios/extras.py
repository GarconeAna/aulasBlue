
#########################

# 9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma 
# dos quadrados dos elementos do vetor.

vetorA = [3, 4, 5, 6, 7, 9, 13, 14, 16, 19]
soma = 0

for i in vetorA :
    soma += i**2
print(soma)
print()

# 10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor 
# de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois 
# outros vetores.

# 11.Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

# 12.Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos 
# alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

# 13.Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média 
# anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

# 14.Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# a."Telefonou para a vítima?"
# b."Esteve no local do crime?"
# c."Mora perto da vítima?"
# d."Devia para a vítima?"
# e."Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
# "Inocente".


# 15.Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
# encerrando a entrada de dados quando for informado um valor igual a -1 
# (que não deve ser armazenado). Após esta entrada de dados, faça:
# a.Mostre a quantidade de valores que foram lidos;
# b.Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c.Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# d.Calcule e mostre a soma dos valores;
# e.Calcule e mostre a média dos valores;
# f.Calcule e mostre a quantidade de valores acima da média calculada;
# g.Calcule e mostre a quantidade de valores abaixo de sete;
# h.Encerre o programa com uma mensagem;


# 16.Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com 
# base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas 
# daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana 
# recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa 
# (usando um array de contadores) que determine quantos vendedores receberam salários 
# nos seguintes intervalos de valores:
# a.$200 - $299
# b.$300 - $399
# c.$400 - $499
# d.$500 - $599
# e.$600 - $699
# f.$700 - $799
# g.$800 - $899
# h.$900 - $999
# i.$1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, 
# sem fazer vários ifs aninhados.
