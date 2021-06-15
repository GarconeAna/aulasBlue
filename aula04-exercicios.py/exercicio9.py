#09 Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10 
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

numero = 0,1,2,3,4,5,6,7,8,9,10

import random 
aleatorio = random.choice(numero)

print('Esse é um jogo de adivinhação.\nO computador pensa em um número e você adivinha qual é.')
print('')

aceita = (input('Você aceita esse desafio? HAHAHA [SIM/NÃO]'))
print('')
aceitaTratado = aceita.upper().replace('A' , 'Ã')

if aceitaTratado == 'SIM' :
    escolha = int(input('O computador já pensou! \nAgora é a sua vez, escolha seu numero: [0 a 10]'))
    print('')

    if escolha == aleatorio :
        print('Opa!! Você venceu o computador!!')

    else :
        print('IHH! O computador venceu!')

    print('')
    print(f'O computador escolheu {aleatorio}.\nVocê escolheu {escolha}.')

elif aceitaTratado == 'NÃO' :
    print('POXA.\nEntão, jogo encerrado.')
else :
    print('Opção inválida. Tente novamente.')