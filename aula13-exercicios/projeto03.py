# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos
# até que o usuário diga que não tem mais ninguém para votar, esse programa
# precisa ter duas funções:
# #######A 1° Função autoriza_voto() parâmetro o ano de nascimento de uma pessoa digitado pelo usuário,
# #######retornando voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função votacao() dois parâmetros, autorização (que
# virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, votacao() retorna “Você não pode votar”,
# caso o contrário votacao() deve validar o número que a pessoa escolheu 
# (crie 3 candidatos para a votação) pode escolher de 1 a 5:
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.

# as funções tem que ser criadas primeiro

def autorizaVoto(anoDeNascimento) :
    if (2021 - anoDeNascimento) >= 18 and (2021 - anoDeNascimento) <= 70 :
        # voto obrigatorio
        pass
    elif (2021 - anoDeNascimento) == 16 or (2021 - anoDeNascimento) == 17 and (2021 - anoDeNascimento) > 70 :
        # voto opicional
        pass
    elif 2021 - anoDeNascimento < 16 :
        # voto negado 
        pass

def votacao(retornoDoAutorizaVoto,voto) :
    if retornoDoAutorizaVoto == 'negado' :
        #retornar: 'Você não pode votar'
        pass
    else :
        #validar o numero que foi escolhido
        contCandidato1 = 0
        contCandidato2 = 0
        contCandidato3 = 0
        contVotoNulo = 0
        contVotoBranco = 0
        
        if voto == 1 :
            contCandidato1 += 1
        if voto == 2 :
            contCandidato2 += 1
        if voto == 3 :
            contCandidato3 += 1
        if voto == 4 :
            contVotoNulo += 1
        if voto == 5 :
            contVotoBranco += 1

        
    print(f'{contCandidato1} foi a quantidade de voto(s) que o candidato 1 recebeu.')
    print(f'{contCandidato2} foi a quantidade de voto(s) que o candidato 2 recebeu.')
    print(f'{contCandidato3} foi a quantidade de voto(s) que o candidato 3 recebeu.')
    print(f'{contVotoNulo} foi a quantidade de voto(s) nulo(s).')
    print(f'{contVotoBranco} foi a quantidade de voto(s) em branco.')

    maiorVoto = 0

    if contCandidato1 > contCandidato2 :
        maiorVoto = 1
        if contCandidato1 > contCandidato3 :
            maiorVoto = 1
    elif contCandidato2 > contCandidato3 :
        maiorVoto = 2
    elif contCandidato3 > contCandidato1 :
        maiorVoto = 3

    print(f'Candidato {maiorVoto} foi quem venceu as eleições.')


while True :
    escolhendoDe1a5 = int(input('Escolha o candidato: [1/2/3] \nVoto nulo: [4] \nVoto em branco: [5] '))
    autoriza = 'aprovado'
    votacao(autoriza,escolhendoDe1a5)
    maisVotos = input('Cadastrar mais votos? [SIM/NAO] ')
    if maisVotos == 'NAO' or maisVotos == 'nao' :
        break        

        


    
    