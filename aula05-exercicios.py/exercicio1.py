#1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite seu sexo: [F/M] ').upper()

while sexo != 'F' and sexo != 'M' :
    sexo = print('Resposta inválida. Por favor, digite novamente.')
    sexo = input('Digite seu sexo: [F/M] ').upper()
if sexo == 'F' :
    print(f'Foi digitado {sexo}, correspondendo à feminino.')
elif sexo == 'M' :
    print(f'Foi digitado {sexo}, correspondendo à masculino.')


