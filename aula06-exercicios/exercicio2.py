# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

numero = int(input('Digite um número: '))

for i in range(numero) :
    if i < numero :
        i+=1
        modulo = numero % i
        if modulo == 0 :
            print(f'{i} é divisor de {numero}')


# for i in range(1,numero) :
#     if numero % i == 0 :
#         print(i)

