'''
    Instalar o Live Server para rodar a página.
'''

import time, datetime
import os
from collections import Counter
from datetime import datetime as dt
# import sqlalchemy
# print(sqlalchemy.__version__)

# print(os.listdir("/"))

# with open("leiame.txt") as f:
#     lines = f.readlines()
#     print(lines)

# TENTANTIVA DE REDUZIR O CÓDIGO
# A class Element() não funciona corretamente dentro do loop.
# getID = ['testando', 'emailVoter', 'showMsgEmail', 'showMsgEleitores', 'boxConectar', 'boxPoll', 'numCandidato', 'showMsgVote', 'showTime', 'showPollOk', 'showTitleEnd', 'showRepresentanteEVice', 'showRepresentante', 'showVice', 'showLastMsg', 'representanteNome', 'representanteNumero', 'representanteVotos', 'viceNome', 'viceNumero', 'viceVotos', 'showLastThanks', 'showEleitores']
# for i in range(len(getID)):
#     getID[i] = Element(getID[i])

testando = Element("testando")
emailVoter = Element("emailVoter")
showMsgEmail = Element("showMsgEmail")
showMsgEleitores = Element("showMsgEleitores")
boxConectar = Element("boxConectar")
boxPoll = Element("boxPoll")
numCandidato = Element("numCandidato")
showMsgVote = Element("showMsgVote")
showTime = Element("showTime")
showPollOk = Element("showPollOk")
showTitleEnd = Element("showTitleEnd")
showRepresentanteEVice = Element("showRepresentanteEVice")
showRepresentante = Element("showRepresentante")
showVice = Element("showVice")
showLastMsg = Element("showLastMsg")
representanteNome = Element("representanteNome")
representanteNumero = Element("representanteNumero")
representanteVotos = Element("representanteVotos")
viceNome = Element("viceNome")
viceNumero = Element("viceNumero")
viceVotos = Element("viceVotos")
representanteNome2 = Element("representanteNome2")
representanteNumero2 = Element("representanteNumero2")
representanteVotos2 = Element("representanteVotos2")
viceNome2 = Element("viceNome2")
viceNumero2 = Element("viceNumero2")
viceVotos2 = Element("viceVotos2")
showLastThanks = Element("showLastThanks")
showEleitores = Element("showEleitores")

passwordStop = '987654321'

finalNome = []
finalNumero = []
finalVotos = []
votos = []

eleitores = [
    {'nome': 'Eleitor 01', 'email': 'email1@gmail.com', 'voto': 0},
    {'nome': 'Eleitor 02', 'email': 'email2@gmail.com', 'voto': 0},
    {'nome': 'Eleitor 03', 'email': 'email3@gmail.com', 'voto': 0}
]

candidatos = [
    {'nome': 'Candidato 01', 'numero': 1, 'nascimento': '01/10/1987', 'votos': 0},
    {'nome': 'Candidato 02', 'numero': 2, 'nascimento': '01/10/1988', 'votos': 0},
    {'nome': 'Candidato 03', 'numero': 3, 'nascimento': '01/10/1985', 'votos': 0}
]

# FUNÇÕES COMPLEMENTARES
def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return dt_.strftime(fmt)

def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)

def display(n, a):
    n.element.style.display = a

# Pega valor do input:
# def elementValue(a):
#     a.element.value

# Mostra resultado no browser
def innerText(n, t, i=0):
    if i == 0:
        n.element.innerText = t
    else:
        n.element.innerText += t
    
# Para fins de testes.
for k in eleitores:
    nome_eleitor = k['nome']
    email_eleitor = k['email']
    innerText(showEleitores, f' Email: {email_eleitor}.', 1)

def ordenado_mais_antigo(n):
    t = {k: v for k, v in sorted(n.items(), key=lambda item: item[1])}
    for (key,value) in t.items():
        finalNome.append(key) # Armazena o nome do candidato em uma variável.
        finalNumero.append(value[1]) # Armazena o número do candidato em uma variável.
        finalVotos.append(value[2]) # Armazena os votos do candidato em uma variável.

# LOGAR
def login(*ags):
    check_eleitor = 0
    eleitor_email = emailVoter.element.value
    if eleitor_email != passwordStop:
        for key_eleitor in eleitores:
            if eleitor_email == key_eleitor['email']:
                check_eleitor = 1
                if key_eleitor['voto'] == 0:
                    key_eleitor['voto'] = 1
                    display(boxConectar, 'none')
                    display(showMsgEmail, 'none')
                    display(showMsgEleitores, 'block')
                    innerText(showMsgEleitores, f'Seja bem-vindo(a) {key_eleitor["nome"]}!\n\nSEGUEM ABAIXO OS CANDIDATOS:\n\n')

                    for k in candidatos:
                        innerText(showMsgEleitores, f'{k["nome"]}, NÚMERO: {k["numero"]}\n', 1)

                    # Aqui libera o botão para votar
                    display(boxPoll, 'block')
                    display(showPollOk, 'none')
                else:
                    display(showTime, 'block')
                    display(showMsgEmail, 'block')
                    innerText(showTime, f'{now()}')
                    innerText(showMsgEmail, f'Você já votou! Por favor, deixe o próximo votar.')
    else:
        check_eleitor = 1
        display(boxConectar, 'none')
        display(showPollOk, 'block')
        innerText(showPollOk, f'FIM DA VOTAÇÃO!')
        calcFinal(eleitor_email)

    if check_eleitor == 0:
        display(showMsgEmail, 'block')
        innerText(showMsgEmail, f'Não encontramos seu email. Por favor, tente novamente.')
        display(showPollOk, 'none')

    emailVoter.clear()

# VOTAÇÃO
def poll(*ags):
    emailVoter.clear()
    n = int(numCandidato.element.value)
    check_votou = 0
    for k in candidatos:
        numero_candidato = k['numero']
        if n == numero_candidato:
            votos.append(numero_candidato)
            k['votos'] = k['votos']+1 # Adiciona 1 voto para o candidato escolhido
            check_votou = 1
            display(showMsgVote, 'none')
            display(showMsgEleitores, 'none')
            display(boxPoll, 'none')
            display(showPollOk, 'block')
            innerText(showPollOk, f'VOCÊ VOTOU! Obrigado!\n\n')

            # Check se todos os eleitores já votaram.
            check_parar_votacao = 0
            for key in eleitores:
                if key['voto'] == 0:
                    check_parar_votacao = 1
                    display(boxConectar, 'block')
                    break
                else:
                    check_parar_votacao = 0

            if check_parar_votacao == 0:
                display(boxConectar, 'none')
                display(showPollOk, 'block')
                innerText(showPollOk, f'Todos já votaram.\nFim da votação!')
                calcFinal(0)
            break
    if check_votou:
        check_votou = 0
    else:
        display(showMsgVote, 'block')
        innerText(showMsgVote, f'Você digitou um número errado.\nPor favor, digite o número de um dos candidatos!')

    numCandidato.clear()

# INÍCIO DOS CÁLCULOS
def calcFinal(passStop):
    ninguem_votou = 0
    nascimento_timestamp = {}
    dict = {}
    primeiro = []
    
    if passStop != passwordStop:
        votos_repetidos = Counter(votos)
    else:
        # Check se algum eleitor votou.
        for key in eleitores:
            if key['voto'] == 1:
                check_parar_votacao = 1
                break
            else:
                check_parar_votacao = 0

        if check_parar_votacao == 0:
            ninguem_votou = 1
            for k in candidatos:
                votos.append(k['numero'])
                k['votos'] = 0

        votos_repetidos = Counter(votos)

    for value in votos_repetidos.values(): # Cria uma lista vazia apenas com os voto repetido.
        dict[value] = []

    for (key,value) in votos_repetidos.items(): # Adiciona na lista o(s) número(s) de repetições de cada voto.
        dict[value].append(key)

    maxVote = sorted(dict.keys(),reverse=True)[0] # Pega o(s) número(s) da(s) quantidade(s) mais votada(s).
    empates = len(dict[maxVote]) # Conta quantos números estão empatados. No caso: 7

    display(showTitleEnd, 'block')

    if empates > 1: # Se houve empate entra aqui.
        for d in dict[maxVote]: # Percorre cada elemento da lista.
            for c in candidatos: # Percorre cada elemento da lista.
                if c['numero'] == d: # Compara o número da lista de votados com a relação de candidatos para pegar outras informações.
                    # Adidiciona a data de nascimento (em timestump) no nome do candidato.
                    nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

        ordenado_mais_antigo(nascimento_timestamp)
        display(showRepresentanteEVice, 'block')
        innerText(representanteNome, finalNome[0])
        innerText(representanteNumero, finalNumero[0])
        innerText(representanteVotos, finalVotos[0])
        innerText(viceNome, finalNome[1])
        innerText(viceNumero, finalNumero[1])
        innerText(viceVotos, finalVotos[1])
    else: # Se não houve empate entra aqui para encontrar o segundo colocado.
        for d in dict[maxVote]: # Percorre cada elemento da lista.
            for c in candidatos: # Percorre cada elemento da lista.
                if c['numero'] == dict[maxVote][0]: # Compara o número da lista de votados com a relação de candidatos para pegar outras informações.
                    nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

        for (key, value) in nascimento_timestamp.items():
            primeiro = [key, value[0], value[1], value[2]] # Armazena o primeiro colocado em uma variável.
            break

        display(showRepresentante, 'block')
        innerText(representanteNome2, primeiro[0])
        innerText(representanteNumero2, primeiro[2])
        innerText(representanteVotos2, primeiro[3])

        # Verifica se os votos não foram unânimes.
        if len(votos_repetidos) > 1:
            del dict[maxVote] # Remove o mais votado para descobrir o segundo.
            maxVote = sorted(dict.keys(),reverse=True)[0] # Pega o(s) número(s) da(s) quantidade(s) mais votada(s).
            nascimento_timestamp = {} # Resetar o dict

            for d in dict[maxVote]: # Percorre cada elemento da lista.
                for c in candidatos: # Percorre cada elemento da lista.
                    if c['numero'] == d: # Compara o número da lista de votados com a relação de candidatos para pegar outras informações.
                        nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

            ordenado_mais_antigo(nascimento_timestamp)
            display(showVice, 'block')
            innerText(viceNome2, finalNome[0])
            innerText(viceNumero2, finalNumero[0])
            innerText(viceVotos2, finalVotos[0])
        else:
            # Se foi unânime, ele sorteia o mais antigo para ser o vice.
            for c in candidatos: # Percorre cada elemento da lista.
                # Adidiciona a data de nascimento (em timestump) no nome do candidato.
                nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

            n_ordenado = {k: v for k, v in sorted(nascimento_timestamp.items(), key=lambda item: item[1])}
            for (key,value) in n_ordenado.items():
                if value[1] != primeiro[2]: # Quando o valor atual for diferente do primeiro colocado, ele imprime e finaliza.
                    display(showVice, 'block')
                    innerText(viceNome2, f'{key}')
                    innerText(viceNumero2, f'{value[1]}')
                    innerText(viceVotos2, f'{value[2]}')
                    break

    if ninguem_votou:
        display(showLastMsg, 'block')
        display(showLastThanks, 'block')
        innerText(showLastMsg, f'NÃO HOUVERAM ELEITORES, PORTANTO, O SISTEMA SELECIONOU POR IDADE OS CANDIDATOS VENCEDORES.\n\n')
    else:
        display(showLastThanks, 'block')
