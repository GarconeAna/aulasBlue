#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

# listaVazia = []

# while True :
#     num = int(input('Digite o número: '))
#     if num not in listaVazia :
#         listaVazia.append(num)
#         continuar = input('Deseja continuar? [SIM/NAO] ')
#         if continuar == 'nao' :
#             break

# listaVazia.sort()
# print(listaVazia)

############################
# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

# lOriginal = []
# lPares = []
# lImpares = []

# while True :
#     n = int(input('Digite o número: '))
#     if n not in lOriginal :
#         lOriginal.append(n)
#         if n % 2 == 0 :
#             lPares.append(n)
#         elif n % 2 != 0 :
#             lImpares.append(n)
#         cont = input('Deseja continuar? [SIM/NAO] ')
#         if cont == 'nao' :
#             break

# print(lOriginal)
# print(lPares)
# print(lImpares)

############################
# #Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# import random 

# num = list(range(1,61))
# quantidadeJogos = int(input('Quantos jogos? '))

# listaMega = []

# while len(listaMega) < quantidadeJogos :
#     listaDentro = []

#     while len(listaDentro) < 6 :
#         numAleatorio = random.choice(num)
#         if numAleatorio not in listaDentro :
#             listaDentro.append(numAleatorio)
#     listaMega.append(listaDentro)
    
# print(listaMega)

############################

# vetorList = [1, 4, 9, 22, 18]
 
# i = 0
# while i < len(vetorList):
#     print(vetorList[i])
#     i = i + 1

