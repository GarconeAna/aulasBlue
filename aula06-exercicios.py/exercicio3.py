# 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de
# passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de
# acordo com o intervalo passado.

numeroInicio = int(input('Digite o número inicial: '))
numeroFim = int(input('Digite o número final: '))
numeroIntervalo = int(input('Digite o número de intervalo entre os números digitados anteriormente: '))

for i in range(numeroInicio,numeroFim,numeroIntervalo) :
    print(i)