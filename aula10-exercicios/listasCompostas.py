# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade

# listaComposta = []
# contMaiores = 0
# contMenores = 0

# for i in range(5) :
#     nome = input('Digite o nome: ')
#     idade = int(input('Digite a idade: '))

#     listaNome = []

#     listaNome.append(nome)
#     listaNome.append(idade)

#     listaComposta.append(listaNome)


# print()
# print(listaComposta)
# print()

# for n in listaComposta :
#     if n[1] > 18: 
#         print(f'{n[0]} é maior de idade')
#         contMaiores += 1
#     else :
#         print(f'{n[0]} é menor de idade')
#         contMenores += 1
# print()
# print(f'{contMaiores} cliente(s) maior(es) de idade.')
# print(f'{contMenores} cliente(s) menor(es) de idade.')

# 2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista,
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o
# programa. No final mostre:
# # Quantas pessoas foram cadastradas
# # Mostre a maior altura
# # Mostre a menor altura

# lista = []
# contCadastros = 0
# maiorAltura = 0
# menorAltura = 4.00

# while True :
#     contCadastros += 1
#     nome = input('Digite o nome: ')
#     lista.append(nome)


#     altura = float(input('Digite a altura: '))
#     lista.append(altura)
#     if altura > maiorAltura :
#         maiorAltura = altura 
#     elif altura < menorAltura :
#         menorAltura = altura

#     inserirDados = input('Deseja continuar? [SIM/NAO]')
#     if inserirDados == 'nao' or inserirDados == 'NAO' :
#         break

# print(f'{contCadastros} cadastro(s) feito(s).')
# print(f'{maiorAltura:.2f}m é a maior altura cadastrada.')
# print(f'{menorAltura:.2f}m é a menor altura cadastrada.')