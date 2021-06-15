#08 O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais.
#Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1
#Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


x = int(input())

nota100 = x // 100
nota50 = (x % 100) // 50 
nota10 = (x % 50) // 10 
nota5 = (x % 10) // 5 
nota1 = (x % 5) % 5

if x < 10 or x > 600 :
    print('O valor mínimo é de R$10 e o máximo é de R$600.\nPor favor, tente novamente.')
else :
    print(f'{nota100:.0f} nota(s) de R$100')
    print(f'{nota50:.0f} nota(s) de R$50')
    print(f'{nota10:.0f} nota(s) de R$10')
    print(f'{nota5:.0f} nota(s) de R$5')
    print(f'{nota1:.0f} nota(s) de R$1')