#07 Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#até R$ 280,00 (incluindo) : aumento de 20%
#entre R\$ 280,00 e R$ 700,00 : 15%
#entre R\$ 700,00 e R$ 1500,00 : 10%
#R$ 1500,00 em diante : 5%
#na tela: salário antes;percentual de aumento;valor do aumento;novo salário

percentual = 0
aumento = 0
reajuste1 = 20
reajuste2 = 15
reajuste3 = 10
reajuste4 = 5 

salarioAtual = float(input('Digite o valor do seu salário atual: '))

if salarioAtual <= 280.00 :
    percentual = reajuste1 / 100 
    aumento = percentual * salarioAtual
    salarioNovo = salarioAtual + aumento 
elif salarioAtual < 700.00 :
    percentual = reajuste2 / 100 
    aumento = percentual * salarioAtual
    salarioNovo = salarioAtual + aumento
elif salarioAtual < 1500.00 :
    percentual = reajuste3 / 100
    aumento = percentual * salarioAtual
    salarioNovo = salarioAtual + aumento
elif salarioAtual >= 1500.00 :
    percentual = reajuste4 / 100
    aumento = percentual * salarioAtual
    salarioNovo = salarioAtual + aumento

print(f'Seu salário atual é R$ {salarioAtual}\nPercentual de aumento: {percentual * 100}%')
print(f'Valor do aumento: R$ {aumento}\nSeu salário novo é R$ {salarioNovo}')