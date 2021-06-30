# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)

quantidade = int(input('Quantos números serão somados? '))
lista = []
for i in range(quantidade) :
    num1 = int(input('Qual o número da vez? '))
    lista.append(num1)

soma = sum(lista)
print(f'O resultado da soma dos número digitados é: {soma}')