### 1 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
# (que podem ser armazenados em uma lista) e seus valores correspondentes 
# aos quadrados desses números.

# listaNum = [1, 4, 5, 6, 7, 9]
# numDicionario = dict()
# for i in listaNum :
#     numDicionario[i] = i**2
# print(numDicionario)
# print()


### 2 – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] 
# e cada valor associado é o número ao quadrado.


# numDicionario2 = dict()
# for n in range(1,11) :
#     numDicionario2[n] = n**2
# print(numDicionario2)
# print()

### 2.1 com input 

# numero = int(input('Digite até que valor para calcular ao quadrado: '))
# numDicionario3 = dict()
# for q in range(1,numero+1) :
#     numDicionario3[q] = q**2
# print(numDicionario3)

############################################ ainda não consegui resolver certinho

### 3 - Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​
# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​
# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

# estoqueLista = [('melancia',4),('carne',0),('agua',1),('refrigerante',0),('cafe',8)]
# estoque = dict(estoqueLista)

# while True :
#     mercado = input('Deseja comprar [SIM]? Ou [0] para sair do mercado: ')
#     if mercado == '0' :
#         break
#     elif mercado != '0' :
#         escolhaDeItens = input('O que deseja comprar? ')
#         quantidadeNoEstoque = estoque.pop(escolhaDeItens,'Produto inválido.')
#         if quantidadeNoEstoque == 'Produto inválido.' :
#             print('Produto inválido')
#         else :
#             if quantidadeNoEstoque == 0 :
#                 print('Produto indisponível.')
#             else :
#                 escolhaDeQuantidade = int(input(f'Quantos {escolhaDeItens} deseja comprar? '))
#                 if quantidadeNoEstoque < escolhaDeQuantidade :
#                     print('Quantidade solicitada não disponível.')

############################################ ainda não consegui resolver certinho

# correção do exercicio 03 pelo professor

itensComprados = []
totalQuantidadeGeral = []

estoque = {'coca':15, 'chocolate':5, 'batata':11, 'papel':3, 'presunto':26}

continuar = input('Bem vindo ao Supermercado T3C5. Deseja ir as commpras? ')
while continuar not in ['s','n'] :
    continuar = input('Resposta inválida. Deseja ir nas compras (s/n) ').lower()

while continuar == 's':
    print()
    print('Nossos produtos:')

    for i in estoque:
        if estoque[i] > 0:
            print(i)
    
    print()

    produto = input

    continuar = input('Deseja continuar as compras? (s/n) ').lower()
    while continuar not in ['s','n'] :
        continuar = input('Resposta inválida. Deseja ir nas compras (s/n) ').lower()
