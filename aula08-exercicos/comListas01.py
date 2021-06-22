# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente


l = [5, 7, 2, 9, 4, 1, 3]
tamanho = len(l)
maior = max(l)
menor = min(l)
soma = sum(l)
crescente = sorted(l) 
l.reverse()


print(f'O tamanho da lista é {tamanho}')
print(f'O maior valor da lista é {maior}')
print(f'O maior valor da lista é {menor}')
print(f'A soma dos valores da lista é {soma}')
print(f'A ordem crescente da lista é {crescente}')
print(f'A ordem decrescente da lista é {l}')