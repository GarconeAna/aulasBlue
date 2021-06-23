# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

dicionarioAluno = dict()
nomeAluno = input('Digite o nome do aluno: ')
notaAluno = float(input('Digite a nota do aluno: ').replace(',','.'))
situacao = ''
if notaAluno >= 7 and notaAluno <= 10:
    situacao = 'aprovado(a)'
elif notaAluno < 7 and notaAluno >= 5:
    situacao = 'recuperação'
else:
    situacao = 'reprovado'
dicionarioAluno[nomeAluno] = [notaAluno, situacao]

for i in dicionarioAluno:
    print(f'Aluno(a) {i} tem a nota média {dicionarioAluno[i][0]}. Situação: {dicionarioAluno[i][1]}')