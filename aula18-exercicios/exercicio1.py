# Exercício de Fixação 1 – Classe Bomba de Combustível
# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – 
# método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo.
# ii. abastecerPorLitro( ) – 
# método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# iii. alterarValor( ) – 
# altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – 
# altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – 
# altera a quantidade de combustível restante na bomba.
##### OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. ######

class BombaCombustivel : 
    def __init__(self, valorLitro, quantidadeCombustivel, tipoCombustivel='gasolina') :
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = 5.78
        self.quantidadeCombustivel = 15000

    def abastecerPorValor(self) :
        valor =  int(input('Valor a ser abastecido em reais: '))
        combustivelNoVeiculo = self.valorLitro * valor
        return combustivelNoVeiculo

    def abastecerPorLitro(self) :
        litros =  int(input('Quantidade a ser abastecido em litros: '))
        valorParaPagar = self.valorLitro * litros
        return valorParaPagar

    def alterarValor(self) :
        pass

    def alterarCombustivel(self) :
        pass

    def alterarQuantidadeCombustivel(self) :
        pass