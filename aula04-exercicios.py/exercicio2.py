#02 Faça um programa que pergunte ao usuário um número e valide se o numero é par ou impar:
numero = int(input('Digite um número: '))

imparOuPar = numero % 2

if imparOuPar == 0 :
    print('O número digitado é par.')
else :
    print('O número digitado é impar.')
