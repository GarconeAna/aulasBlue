#03 peça um valor e mostre na tela se o valor é positivo ou negativo. não aceitar o número 0
valor = int(input('Digite um valor: '))

if valor > 0 :
    print('Esse número é positivo')
elif valor == 0 :
    print('Valor não permitido.')
else :
    print('Esse número é negativo') 
