#4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10(fixo). O jogador vai tentar 
#adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram 
#necessários para vencer
#mostrar se foi mais perto ou mais longe de vencer 


import random 
aleatorio = random.randint(0, 10)
palpites = 0

resp = int(input('Adivinhe qual número o computador escolheu: '))

while resp != aleatorio :
    resp = int(input('Rsposta errada. Escolha outra vez: '))
    palpites += 1
if resp == aleatorio :
    print(f'Foram necessário {palpites} palpite(s) para ganhar.')
    