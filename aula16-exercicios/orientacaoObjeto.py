class Manifero() :
    # criando o metodo construtor, ele vai servir para ja passar todos 
    # os atributos para os objetos que eu estou criando
    def __init__(self, nome, pelo, cor, tamanho, idade) :
        self.nome = nome
        self.pelo = pelo
        self.cor = cor
        self.tamanho = tamanho
        self.idade = idade

    def crescer(self) :
        self.idade += 1

    def locomover(self) :
        print('Elx esta andando')
    
    def comer(self) :
        self.tamanho = 'grande'


cachorro = Manifero('Lili', 'curto', 'marrom', 'medio', 4)
print(vars(cachorro))

cachorro.crescer()
cachorro.locomover()
cachorro.comer()
print(vars(cachorro))
print()
print(cachorro.nome) 

# 1.a) Crie uma classe pessoa com os seguintes atributos: nome,
# sobrenome e idade.
# 1.b) Acrescente a classe criada um método para mostrar os dados de
# uma pessoa.
# 1.c) Crie um objeto do tipo pessoa para testar suas propriedades e
# métodos

class Pessoa() :
    def __init__(self, nome, sobrenome, idade) :
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade 
    
    def dados(self) :
        print(f'Nome: {self.nome} {self.sobrenome}\nIdade: {self.idade} anos')
        # return ''

dadoPessoa = Pessoa('Ana Carolina', 'Garcone de Vasconcelos', 19)
dadoPessoa.dados()
#guardar = dadoPessoa.

#2) Crie uma classe chamada Conta para simular as operações de
#uma conta corrente. Sua classe deverá ter os atributos Titular e
#Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe
#Conta e teste os atributos e métodos implementados.





