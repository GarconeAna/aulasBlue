#2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
#corretamente a senha. A senha é “Blue123”
#2b - Exiba quantas vezes o usuário errou a digitação.

senha = input('Digite sua senha: ')
erros = 0

while senha != 'Blue123' :
    senha = input('Senha errada. Digite sua senha: ')
    erros += 1
print(f'Foi digitado {erros} a senha errada.')