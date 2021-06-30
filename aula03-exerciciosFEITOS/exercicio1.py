#01 calculadora de conversão de moedas 
# preciso pedir um valor 
# preciso também saber quais são os valores das moedas 
# para converter tenho que pegar o valor que queremos converter e dividir pelo valor da moeda

dolar = 5.04
euro = 6.13
libraEsterlina = 7.13
dolarCanadense = 4.16
pesoArgentino = 0.053
pesoChileno = 0.0070

nome = input('Digite seu nome: ')
print(f'Olá, {nome}. Vamos converter seu dinheiro?')
valorEmReais = float(input('Por favor, Digite o valor para convertermos: '))

print(f'Valor em dolar: ${(valorEmReais / dolar):.2f}')
print(f'Valor em euro: €{(valorEmReais / euro):.2f}')
print(f'Valor em libra esterlina: £{(valorEmReais / libraEsterlina):.2f}')
print(f'Valor em dolar canadense: ${(valorEmReais / dolarCanadense):.2f}')
print(f'Valor em peso argentino: ${(valorEmReais / pesoArgentino):.2f}')
print(f'Valor em peso chileno: ${(valorEmReais / pesoChileno):.2f}')