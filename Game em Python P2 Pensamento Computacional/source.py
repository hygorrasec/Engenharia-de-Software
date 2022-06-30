"""
Curso: Engenharia de Software
Período: 1o
Disciplina: Pensamento Computacional
Grupo: Fabrício Souza, Hygor Rasec e Victor Bernardo
Tema escolhido: Game em Python no estilo RPG.
Versão: 1.8

====================================================

INFORMAÇÕES IMPORTANTES PARA FINS DE ESTUDO:
# from os import listdir, chdir, getcwd
# from os.path import join

# listdir() -> Listando arquivos e diretórios
# chdir() -> Muda o diretório.
# getcwd() -> Retorna o caminho absoludo.
# join() -> Recebe dois parâmetros, sendo o primeiro diretório atual e o segundo o diretório que será juntado ao atual.
# eval() -> Converte string em formato de lista para uma lista real.

# LISTAR APENAS ARQUIVOS
# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
# print(onlyfiles)

# dicionario = {}
# dicionario['chave'] = 'valor' -> Adiciona ou atualiza um dado no dicionário.

# scanner = os.scandir('accounts')  # Listando arquivos e diretórios com mais detalhes
# arquivos = list(scanner)
# print(arquivos[0].inode())  # Identificador do elemento na árvore do diretório.
# print(arquivos[0].is_dir())  # É um diretório?
# print(arquivos[0].is_file())  # É um arquivo?
# print(arquivos[0].is_symlink())  # É um link simbólico?
# print(arquivos[0].name)  # Nome do arquivo.
# print(arquivos[0].path)  # Caminho até o arquivo.
# print(arquivos[0].stat())  # Estatísticas do arquivo.
# scanner.close()  # Precisa fechar o scandir

"""

# Manipulando arquivos do SO.
from random import choice, randrange, randint
import json

data_default = {
                    'username': '',
                    'password': '',
                    'level': '1',
                    'health': '100',
                    'exp': '0',
                    'first': '1',
                    'atkMin': '10',
                    'atkMax': '20'
                }

def entrar():
    global usuario
    account_ok = 0
    password_ok = 0
    print('ENTRAR:\n')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

    with open('accounts.json', encoding='utf-8') as acc:
        accounts = json.load(acc)

    for account in accounts:
        if usuario.lower() == account['username'].lower():
            account_ok = 1
            if int(senha) == int(account['password']):
                print(f'\nVOCÊ ENTROU COM O USUÁRIO: {account["username"]}!\n')
                password_ok = 1
                break

    if account_ok == 0:
        print('\nNão encontramos nenhuma conta com esse registro.\n')
        menu()
    else:
        if password_ok == 0:
            print('\nVocê digitou uma senha errada.\n')
            menu()
        else:
            game()


def check_accounts():
    '''Quando vazio, iniciar o accounts.json com uma lista vazia.'''
    account_list = []
    
    with open('accounts.json', encoding='utf-8') as acc:
        accounts = json.load(acc)

    for account in accounts:
        account_list.append(account['username'])
    
    print(f'Total de account(s) registrada(s): {len(account_list)}\nAccount(s): {account_list}\n')


def registro():
    while True:
        print('REGISTRO:\n')
        check = 0

        check_accounts()

        usuario = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')
        if usuario != '':
            if senha != '':
                with open('accounts.json', encoding='utf-8') as acc:
                    accounts = json.load(acc)

                for account in accounts:
                    if usuario.lower() == account['username'].lower():
                        print('\nATENÇÃO! Usuário já registrado. Tente outro nome.\n')
                        check = 1

                if check == 0:
                    with open('accounts.json', encoding='utf-8') as acc:
                        accounts = json.load(acc)

                    data_default['username'] = usuario
                    data_default['password'] = senha
                    accounts.append(data_default)

                    with open('accounts.json', "w", encoding="utf-8") as acc:
                        json.dump(accounts, acc, ensure_ascii=False, indent=4, separators=(",", ": ")) 

                    print('\nRegistro realizado com sucesso!\n')
                    check_accounts()
                    menu()
                    break
                else:
                    menu()
                    break
            else:
                print('\nPor favor, digite uma senha válida.\n')
        else:
            print('\nPor favor, digite um usuário válido.\n')


def menu():
    while True:
        opc = ""
        print("""Digite um número de acordo com o que deseja fazer:

    1 - Entrar
    2 - Criar uma nova conta
    3 - Sair
        """)
        opc = input('Escolha uma das opções: ')
        try:
            print('')
            if int(opc) == 1:
                entrar()
                break
            elif int(opc) == 2:
                registro()
                break
            elif int(opc) == 3:
                print('Até a próxima!\n')
                break
        
        except ValueError as err: 
            if opc != 1 or opc != 2 or opc != 3 or err:
                print('Por favor digite apenas os numeros apresentados no menu.\n')


def introducao():
    print('''
Olá, jogador! Seja bem-vindo ao Delta AVA Game! Vamos iniciar sua jornada...
Se você já tem uma jornada, digite 1 para entrar. Caso seja um novo aventureiro, digite 2 para criar sua conta ou digite 3 para sair.
       ''')
    menu()


def read_accounts():
    global user_account
    with open('accounts.json', encoding='utf-8') as acc:
        accounts = json.load(acc)

    for account in accounts:
        if usuario.lower() == account['username'].lower():
            user_account = account
            break

    return user_account


def read_enemies():
    with open('enemies.json', encoding='utf-8') as en:
        enemies = json.load(en)

    return enemies


def search_battle():
    global enemy
    enemy = choice(read_enemies())

    print(f'Você acabou de encontrar {enemy["pre2"]} {enemy["name"]}!')
    print(f'=========================================')

    fight = input('Deseja continuar com esta batalha? (S para sim ou N para não): ')
    try:
        print('')
        if fight.upper() == 'S':
            # battle()
            print('ESTAMOS EM CONSTRUÇÃO...')
            game()
        elif fight.upper() == 'N':
            game()
    
    except ValueError as err: 
        if fight.upper() != 'N' or fight.upper() != 'S' or err:
            print('Por favor digite apenas as letras apresentadas no menu.\n')


def battle():
    turn = ['enemy', 'player']
    if turn[randrange(len(turn))] == 'player':
        while True:
            read_accounts()
            player_health = user_account['health']
            player_exp = user_account['exp']
            player_atkMin = user_account['atkMin']
            player_atkMax = user_account['atkMax']
            player_dmg = randint(player_atkMin, player_atkMax)
            enemy_new_health = int(enemy["health"]) - player_dmg
            if enemy_new_health <= 0:
                enemy_new_health = 0
                print(f'Seu dano {enemy["pre"]} {enemy["name"]} foi {player_dmg} e você o matou.')
                break
            else:
                print(f'Seu dano {enemy["pre"]} {enemy["name"]} foi {player_dmg} e deixou com {enemy_new_health} de vida.')

            player_new_health = player_health - int(enemy['atk'])
            player_new_exp = player_exp + int(enemy["exp"])

            print(f'O(a) {enemy["name"]} te deu um dano de {int(enemy["atk"])}.\n')
            print(f'=========================================')
            print(f'Sua vida era {player_health} e passou a ser {player_new_health}. Você ganhou {int(enemy["exp"])} de experiência.\n')

            user_account['health'] = player_new_health
            user_account['exp'] = player_new_exp


            # BREAK PROVISÓRIO PARA INTERROMPER O LOOP INFINITO
            break


def status_player():
    print('Status do seu personagem:')
    print('=========================')

    read_accounts()
    for k, v in user_account.items():
        print(f'{k}: {v}')

    print('')


# def update_data():
#     for account in listdir('accounts'):
#         if usuario == account.split(extension_data)[0]:
#             chdir(join(getcwd(), 'accounts'))
#             with open(usuario + extension_data, 'w') as arquivo:
#                 arquivo.write(f'{user_account}')

#             chdir('..')


def game():
    # cache = 0
    # Verificar se os dados estão ok.
    # read_accounts()

    # for k, v in data_default.items():
    #     if k not in user_account.keys():
    #         user_account[k] = v
    #         print(f'A chave "{k}" com o valor "{v}" foi adicionado.')
    #         cache = 1

    # if cache:
    #     update_data()
    #     print('Dados Default foram atualizados.\n')

    status_player()

    while True:
        print("""Você está no jogo, escolha o que deseja fazer:

    1 - Status
    2 - Procurar batalha
    3 - Sair
        """)
        opc = input('Escolha uma das opções: ')
        try:
            print('')
            if int(opc) == 1:
                status_player()
            elif int(opc) == 2:
                search_battle()
            elif int(opc) == 3:
                print('Até a próxima!\n')
                break
        
        except ValueError as err: 
            if opc != 1 or opc != 2 or opc != 3 or err:
                print('Por favor digite apenas os numeros apresentados no menu.\n')


introducao()
