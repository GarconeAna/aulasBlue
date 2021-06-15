#01a exercicio para entender o fatiamento
stringA = 'os limites só existem se você os deixar existir.(goku)'
print(len(stringA))
print(stringA[48:54])

#01 media do aluno e dizendo se ele foi aprovado ou não
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print(media) #coloque print(str(media)) isso é boas praticas, mudar numeros para str 
if media >= 6 :
    print('Aluno aprovado!')
else :
    print('Aluno reprovado. Estude mais!')
print('Programa encerrado xD')