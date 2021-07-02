class Funcionario: 
    def __init__(self, nome, cargo, valorHoraTrabalhada) :
        self.nome = nome
        self.cargo = cargo
        self.valorHoraTrabalhada = valorHoraTrabalhada
        self.__horasTrabalhadas = 0
        self.__salario = 0

    @property
    def salario(self) :
        return self.__salario

    @salario.setter
    def salario(self, novoValor) :
        raise ValueError('Use o método apropriado. calculoSalario')


    def registraHoraTrabalhada(self) :
        self.__horasTrabalhadas += 1
    
    def calculoSalario(self) :
        self.__salario = self.__horasTrabalhadas * self.valorHoraTrabalhada


eduardo = Funcionario('Eduardo', 'Dev. Senior', 100)
print(vars(eduardo))
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.registraHoraTrabalhada()
eduardo.calculoSalario()
print(vars(eduardo))
print(eduardo.salario) #chamado com se fosse um atributo, mas é metodo
####### eduardo.salario = 500 # o setter não me deixa alterar o valor pois esta protegido pelo setter
# obriga a usar o metodo apropriado que eu criei