'''
    Instalar o Live Server para rodar a página.
'''

import time, datetime
from collections import Counter
from datetime import datetime as dt
# import sqlalchemy
# print(sqlalchemy.__version__)

# Pega a matrícula do input: mat_voter.element.value
# Mostra na página o resultado: showMsgMat.element.innerText

testando = Element("testando")

mat_voter = Element("mat_voter")
showMsgMat = Element("showMsgMat")
showMsgEleitores = Element("showMsgEleitores")
box_conectar = Element("box_conectar")
box_poll = Element("box_poll")
num_candidato = Element("num_candidato")
showMsgVote = Element("showMsgVote")
showTime = Element("showTime")
showPollOk = Element("showPollOk")
showTitleEnd = Element("showTitleEnd")
showRepresentanteVice = Element("showRepresentanteVice")
showRepresentante = Element("showRepresentante")
showVice = Element("showVice")
showLastMsg = Element("showLastMsg")
representanteNome = Element("representanteNome")
representanteNumero = Element("representanteNumero")
representanteVotos = Element("representanteVotos")
representanteViceNome = Element("representanteViceNome")
representanteViceNumero = Element("representanteViceNumero")
representanteViceVotos = Element("representanteViceVotos")
showLastThanks = Element("showLastThanks")
showEleitores = Element("showEleitores")

passwordStop = 987654321

final_nome = []
final_numero = []
final_votos = []
votos = []

eleitores = []
eleitor01 = {'nome': 'eleitor 01', 'mat': 111, 'voto': 0}
eleitor02 = {'nome': 'eleitor 02', 'mat': 112, 'voto': 0}
eleitor03 = {'nome': 'eleitor 03', 'mat': 113, 'voto': 0}
eleitor04 = {'nome': 'eleitor 04', 'mat': 114, 'voto': 0}
eleitor05 = {'nome': 'eleitor 05', 'mat': 115, 'voto': 0}
eleitor06 = {'nome': 'eleitor 06', 'mat': 116, 'voto': 0}
eleitor07 = {'nome': 'eleitor 07', 'mat': 117, 'voto': 0}
eleitores.append(eleitor01)
eleitores.append(eleitor02)
eleitores.append(eleitor03)
eleitores.append(eleitor04)
eleitores.append(eleitor05)
eleitores.append(eleitor06)
eleitores.append(eleitor07)

for k in eleitores:
    nome_eleitor = k['nome']
    matricula_eleitor = k['mat']
    showEleitores.element.innerText += f' Matrícula: {matricula_eleitor}.'

candidatos = []
candidato01 = {'nome': 'Paulo', 'numero': 1, 'nascimento': '01/12/1987', 'votos': 0}
candidato02 = {'nome': 'Amara', 'numero': 2, 'nascimento': '01/10/1988', 'votos': 0}
candidato03 = {'nome': 'Hygor', 'numero': 3, 'nascimento': '01/05/1989', 'votos': 0}
candidato04 = {'nome': 'Flávia', 'numero': 4, 'nascimento': '01/04/1990', 'votos': 0}
candidato05 = {'nome': 'João', 'numero': 5, 'nascimento': '01/03/1991', 'votos': 0}
candidato06 = {'nome': 'Rafael', 'numero': 6, 'nascimento': '02/04/1992', 'votos': 0}
candidato07 = {'nome': 'Fábio', 'numero': 7, 'nascimento': '02/04/1993', 'votos': 0}
candidatos.append(candidato01)
candidatos.append(candidato02)
candidatos.append(candidato03)
candidatos.append(candidato04)
candidatos.append(candidato05)
candidatos.append(candidato06)
candidatos.append(candidato07)

# FUNÇÕES COMPLEMENTARES
def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return dt_.strftime(fmt)

def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)

def ordenado_mais_antigo(n):
    t = {k: v for k, v in sorted(n.items(), key=lambda item: item[1])}
    for (key,value) in t.items():
        final_nome.append(key) # Armazena o nome do candidato em uma variável.
        final_numero.append(value[1]) # Armazena o número do candidato em uma variável.
        final_votos.append(value[2]) # Armazena os votos do candidato em uma variável.

# LOGAR
def login(*ags):
    check_eleitor = 0
    eleitor_mat = int(mat_voter.element.value)
    if eleitor_mat != passwordStop:
        for key_eleitor in eleitores:
            if eleitor_mat == key_eleitor['mat']:
                check_eleitor = 1
                if key_eleitor['voto'] == 0:
                    # box_conectar.element.remove()
                    box_conectar.element.style.display = 'none'
                    showMsgMat.element.style.display = 'none'
                    showTime.element.style.display = 'block'
                    showTime.element.innerText = f'{now()}'
                    showMsgEleitores.element.style.display = 'block'
                    key_eleitor['voto'] = 1
                    showMsgEleitores.element.innerText = f'Seja bem-vindo(a)!\n\nSEGUEM ABAIXO OS CANDIDATOS:\n\n'
                    for k in candidatos: 
                        nome_candidato = k['nome']
                        numero_candidato = k['numero']
                        showMsgEleitores.element.innerText += f'{nome_candidato}, NÚMERO: {numero_candidato}\n'

                    # Aqui libera o botão para votar
                    box_poll.element.style.display = 'block'
                    showPollOk.element.style.display = 'none'
                else:
                    showTime.element.style.display = 'block'
                    showTime.element.innerText = f'{now()}'
                    showMsgMat.element.style.display = 'block'
                    showMsgMat.element.innerText = f'Você já votou! Por favor, deixe o próximo votar.'
    else:
        check_eleitor = 1
        box_conectar.element.style.display = 'none'
        showPollOk.element.style.display = 'block'
        showPollOk.element.innerText = f'Fim da votação!'
        showTime.element.style.display = 'block'
        showTime.element.innerText = f'{now()}'
        calcFinal(eleitor_mat)

    if check_eleitor == 0:
        showTime.element.style.display = 'block'
        showTime.element.innerText = f'{now()}'
        showMsgMat.element.style.display = 'block'
        showMsgMat.element.innerText = f'Não encontramos sua matrícula. Por favor, tente novamente.'
        showPollOk.element.style.display = 'none'

    mat_voter.clear()

# VOTAÇÃO
def poll(*ags):
    mat_voter.clear()
    n = int(num_candidato.element.value)
    check_votou = 0
    for k in candidatos:
        numero_candidato = k['numero']
        if n == numero_candidato:
            nome_candidato = k['nome']
            votos.append(numero_candidato)
            k['votos'] = k['votos']+1 # Adiciona 1 voto para o candidato escolhido
            check_votou = 1
            showMsgVote.element.style.display = 'none'
            showMsgEleitores.element.style.display = 'none'
            box_poll.element.style.display = 'none'
            showPollOk.element.style.display = 'block'
            showPollOk.element.innerText = f'VOCÊ VOTOU NO CANDIDATO {nome_candidato} NÚMERO {numero_candidato}!\nObrigado!\n\n'
            # Check se todos os eleitores já votaram.
            check_parar_votacao = 0
            for key in eleitores:
                if key['voto'] == 0:
                    check_parar_votacao = 1
                    box_conectar.element.style.display = 'block'
                    break
                else:
                    check_parar_votacao = 0

            if check_parar_votacao == 0:
                box_conectar.element.style.display = 'none'
                showPollOk.element.style.display = 'block'
                showPollOk.element.innerText = f'Todos já votaram.\nFim da votação!'
                calcFinal(0)
            break
    if check_votou:
        check_votou = 0
    else:
        showMsgVote.element.style.display = 'block'
        showMsgVote.element.innerText = f'Você digito um número errado.\nPor favor, digite o número de um dos candidatos!'

    num_candidato.clear()

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

    showTitleEnd.element.style.display = 'block'

    if empates > 1: # Se houve empate entra aqui.
        for d in dict[maxVote]: # Percorre cada elemento da lista.
            for c in candidatos: # Percorre cada elemento da lista.
                if c['numero'] == d: # Compara o número da lista de votados com a relação de candidatos para pegar outras informações.
                    # Adidiciona a data de nascimento (em timestump) no nome do candidato.
                    nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

        ordenado_mais_antigo(nascimento_timestamp)
        showRepresentanteVice.element.style.display = 'block'
        representanteNome.element.innerText = final_nome[0]
        representanteNumero.element.innerText = final_numero[0]
        representanteVotos.element.innerText = final_votos[0]
        representanteViceNome.element.innerText = final_nome[1]
        representanteViceNumero.element.innerText = final_numero[1]
        representanteViceVotos.element.innerText = final_votos[1]
    else: # Se não houve empate entra aqui para encontrar o segundo colocado.
        for d in dict[maxVote]: # Percorre cada elemento da lista.
            for c in candidatos: # Percorre cada elemento da lista.
                if c['numero'] == dict[maxVote][0]: # Compara o número da lista de votados com a relação de candidatos para pegar outras informações.
                    nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

        # showMsgVote.element.style.display = 'block'
        # showMsgVote.element.innerText = f'{nascimento_timestamp}'

        for (key,value) in nascimento_timestamp.items():
            primeiro = [key, value[0], value[1], value[2]] # Armazena o primeiro colocado em uma variável.
            showRepresentante.element.style.display = 'block'
            # representanteNome.element.style.display = 'block'
            # representanteNumero.element.style.display = 'block'
            # representanteVotos.element.style.display = 'block'
            # representanteNome.element.innerText = key
            # representanteNumero.element.innerText = value[1]
            # representanteVotos.element.innerText = value[2]
            showRepresentante.element.innerText = f'REPRESENTANTE:\n{key} com o número {value[1]}. Total de {value[2]} votos(s).\n'

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
            showVice.element.style.display = 'block'
            # representanteViceNome.element.style.display = 'block'
            # representanteViceNumero.element.style.display = 'block'
            # representanteViceVotos.element.style.display = 'block'
            # representanteViceNome.element.innerText = f'{final_nome[0]}'
            # representanteViceNumero.element.innerText = f'{final_numero[0]}'
            # representanteViceVotos.element.innerText = f'{final_votos[0]}'
            showVice.element.innerText = f'VICE-REPRESENTANTE:\n{final_nome[0]} com o número {final_numero[0]}. Total de {final_votos[0]} votos(s).'
        else:
            # Se foi unânime, ele sorteia o mais antigo para ser o vice.
            for c in candidatos: # Percorre cada elemento da lista.
                # Adidiciona a data de nascimento (em timestump) no nome do candidato.
                nascimento_timestamp[c['nome']] = [int(time.mktime(datetime.datetime.strptime(c['nascimento'], "%d/%m/%Y").timetuple())), c['numero'], c['votos']]

            n_ordenado = {k: v for k, v in sorted(nascimento_timestamp.items(), key=lambda item: item[1])}
            for (key,value) in n_ordenado.items():
                if value[1] != primeiro[2]: # Quando o valor atual for diferente do primeiro colocado, ele imprime e finaliza.
                    showVice.element.style.display = 'block'
                    # representanteViceNome.element.style.display = 'block'
                    # representanteViceNumero.element.style.display = 'block'
                    # representanteViceVotos.element.style.display = 'block'
                    # representanteViceNome.element.innerText = key
                    # representanteViceNumero.element.innerText = value[1]
                    # representanteViceVotos.element.innerText = value[2]
                    showVice.element.innerText = f'VICE-REPRESENTANTE:\n{key} com o número {value[1]}. Total de {value[2]} votos(s).'
                    break

    if ninguem_votou:
        showLastMsg.element.style.display = 'block'
        showLastMsg.element.innerText = f'NÃO HOUVERAM ELEITORES, PORTANTO, O SISTEMA SELECIONOU POR IDADE OS CANDIDATOS VENCEDORES.\n\n'
        showLastThanks.element.style.display = 'block'
    else:
        showLastThanks.element.style.display = 'block'
