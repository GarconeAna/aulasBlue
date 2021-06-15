#08 Elabore um programa que recebe dois valores inteiros e mostra se o primeiro valor é maior ou igual ao segundo valor

valor1 = float(input('Por favor, digite o primeiro valor: '))
valor2 = float(input('Por favor, digite o segundo valor: '))

maiorOuIgual = valor1 >= valor2
print(maiorOuIgual)

#08.1 Elabore um programa que recebe dois valores inteiros e mostra se o primeiro valor é maior ou igual ao segundo valor

valor1a = float(input('Por favor, digite o primeiro valor: '))
valor2a = float(input('Por favor, digite o segundo valor: '))

maiorOuIgual2 = valor1a >= valor2a

if maiorOuIgual2:
  print('O primeiro valor digitado é maior ou igual ao segundo valor.')
else:
  print('O segundo valor digitado é maior que o primeiro valor.')