#05 Crie um programa que verifique se uma letra digitada é "F" ou "M". Feminino/Masculino, caso escreva outra letra: Sexo Inválido.
sexo = input('Qual seu sexo? [F/M]') 
respostaTratada = sexo.upper()

if respostaTratada == 'F' :
    print('Feminino.')
elif respostaTratada == 'M' :
    print('Masculino.')
else :
    print('Sexo inválido.')