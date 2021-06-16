#04 Faça um programa que peça dois números, imprima o maior deles ou imprima "Numeros iguais" se os números forem iguais.
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

if valor1 > valor2 :
    print(f'{valor1} é maior que {valor2}.')
elif valor2 > valor1 :
    print(f'{valor2} é maior que {valor1}.')
else :
    print(f'{valor1} é igual a {valor2}.')
