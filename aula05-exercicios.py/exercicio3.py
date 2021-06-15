#3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
#cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No 
#final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos.

idade = 0
sexo = 'sexo'
cont = input('Gostaria de cadastrar? [sim/nao] ')
quantidadeMaior18 = 0
quantidadeMenor20 = 0
quantidadeMasculino = 0

while cont != 'nao' :
    idade = int(input('idade: '))
    while idade > 18 :
        quantidadeMaior18 += 1
    while idade < 20 and sexo == 'F' and sexo == 'f':
        quantidadeMenor20 += 1
    sexo = input('sexo: ')
    while sexo == 'M' and sexo == 'm' :
        quantidadeMasculino += 1
    cont = input('Gostaria de continuar? [sim/nao] ')

print(quantidadeMasculino)
print(quantidadeMaior18)
print(quantidadeMenor20)