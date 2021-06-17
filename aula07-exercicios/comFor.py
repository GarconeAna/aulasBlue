# # Execute as atividades abaixo, utilizando a estrutura de repetição FOR:
# ####01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# # o maior e o menor peso lidos.

maior = 0
menor = 10000

for p in range(5) :
    peso = float(input('Qual peso? '))
    if peso > maior :
        maior = peso 
    if peso < menor : 
        menor = peso 

print(f'O maior peso foi {maior}KG\n O menor peso foi {menor}KG')


# ####02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# # tabuada desse número.

numeroEscolhido = int(input('Qual número para a tabuada? '))
print(f'Tabuada do {numeroEscolhido}:')

for t in range(1,11) :
    print(f'{numeroEscolhido} X {t} = {numeroEscolhido*t}') 


####03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

ano = 0
mes = 0
dia = 0
maiorIdade = 18
quantidadeMaioridade = 0
quantidadeMenoridade = 0


anoAtual = int(input('Digite a data de hoje:\nQue o ano? '))
mesAtual = int(input('Que o mês? '))
diaAtual = int(input('Que o dia? '))

print('Digite a data de nascimento das pessoas:')
for i in range(7) :
    ano = int(input('Que ano nasceu? '))
    mes = int(input('Que mês nasceu? '))
    dia = int(input('Que dia nasceu? '))

    diferencaAno = anoAtual - ano
    diferencaMes = mesAtual - mes
    diferencaDia = diaAtual - dia

    if diferencaMes < 0 :
        diferencaAno = diferencaAno - 1
    elif diferencaMes == 0 :
        if diferencaDia < 0 :
            diferencaAno = diferencaAno - 1
    
    if diferencaAno >= maiorIdade :
        quantidadeMaioridade += 1
    elif diferencaAno < maiorIdade :
        quantidadeMenoridade += 1
    

print(f'{quantidadeMaioridade} pessoa(s) já são maiores.\n{quantidadeMenoridade} pessoa(s) ainda não atigiram maioridade.')

####04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

quantidadePares = 0
soma = 0

for p in range(6) :
    num = int(input('Qual número da vez? '))
    if num % 2 == 0 :
        quantidadePares += 1
        soma = soma + num
    else :
        pass

print(f'A soma dos números pares é {soma}.\nForam digitados {quantidadePares} números pares.')