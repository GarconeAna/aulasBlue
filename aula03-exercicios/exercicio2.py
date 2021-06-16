#Calculadora de aumento de aluguel
# tenho que pedi o valor do aluguel
# tenho que pedi tambem o valor da porcentagem que vai aumentar o aluguel
# valor aluguel e valor aumento
# tenho que dividir o valor aumento por 100 pois é uma porcentagem 
# depois multiplicar pelo valor do aluguel para saber qual sera o aumento
# por ultimo somar o valor do aluguel com o valor do aumento

valorAluguel = float(input('Por favor digite o valor do seu aluguel atual: '))
valorPorcentagem = float(input('Por favor, digite do IGPM: '))
valorAumento = float((valorPorcentagem / 100) * valorAluguel)
valorReajustado = valorAluguel + valorAumento

print(f'Seu aluguel será de: R${valorReajustado:.2f}')