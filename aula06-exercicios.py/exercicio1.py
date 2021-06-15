# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
# quantas vezes aparece as vogais a,e,i,o,u

frase =input('Digite um frase: ')
vogalA = 0 
vogalE = 0
vogalI = 0
vogalO = 0
vogalU = 0


for i in frase :
    if i == 'a' :
        vogalA += 1
    if i == 'e' :
        vogalE += 1
    if i == 'i' :
        vogalI += 1
    if i == 'o' :
        vogalO += 1
    if i == 'u' :
        vogalU += 1
    
print(f'A frase digitada tem {vogalA} vogal(is) "a".')
print(f'A frase digitada tem {vogalE} vogal(is) "e".')
print(f'A frase digitada tem {vogalI} vogal(is) "i".')
print(f'A frase digitada tem {vogalO} vogal(is) "o".')
print(f'A frase digitada tem {vogalU} vogal(is) "u".')
    

 
