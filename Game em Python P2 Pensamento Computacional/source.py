'''

Curso: Engenharia de Software
Período: 1o
Disciplina: Pensamento Computacional
Grupo: Fabrício Souza, Hygor Rasec e Victor Bernardo
Tema escolhido: Game em Python no estilo RPG.
Versão: 2.0

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

'''

from random import choice, randrange, randint
from json import dump, load
from os import stat

accounts_file = 'accounts.json'
enemies_file = 'enemies.json'
data_default_player = {
                    "username": "",
                    "password": "",
                    "level": 1,
                    "health": 100,
                    "healthMax": 100,
                    "exp": 0,
                    "firstLogin": 1,
                    "atkMin": 10,
                    "atkMax": 20,
                    "healthPotion": 1000,
                    "backpack": {},
                    "depot": {},
                    "equips": {
                            "helmet": "Leather Helmet",
                            "armor": "Jacket",
                            "legs": "Leather Legs",
                            "boots": "Leather Boots",
                            "amulet": "",
                            "ring": "",
                            "shield": "Wooden Shield",
                            "weapon": "Axe"
                    },
                }
data_default_enemy = {
                        "name": "Bug",
                        "pre1": "no",
                        "pre2": "o",
                        "pre3": "um",
                        "health": 20,
                        "healthMax": 20,
                        "exp": 100,
                        "atk": 5,
                        "loot": ["Gold Coin"]
                    }

'''
██╗███╗   ██╗████████╗██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗ █████╗  ██████╗ 
██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝██╔══██╗██╔═══██╗
██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║██║   ██║██║     ███████║██║   ██║
██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██║   ██║██║     ██╔══██║██║   ██║
██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗██║  ██║╚██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝                                                                                
'''
def introducao():
    print('''
Olá, jogador! Seja bem-vindo ao Delta AVA Game! Vamos iniciar sua jornada...
Se você já tem uma jornada, digite 1 para entrar. Caso seja um novo aventureiro, digite 2 para criar sua conta ou digite 3 para sair.
       ''')
    menu()

'''
███╗   ███╗███████╗███╗   ██╗██╗   ██╗
████╗ ████║██╔════╝████╗  ██║██║   ██║
██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
'''
def menu():
    while True:
        opc = ''
        print('''\nDigite um número de acordo com o que deseja fazer:

    1 - Entrar
    2 - Criar uma nova conta
    3 - Sair
        ''')
        opc = input('Escolha uma das opções: ')
        try:
            if int(opc) == 1:
                entrar()
                break
            elif int(opc) == 2:
                registro()
                break
            elif int(opc) == 3:
                print(f'\nAté a próxima!\n')
                break
            else:
                error_menu()
        
        except ValueError as err: 
            error_menu()

def error_menu():
    print('\n!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')
    print('| !POR FAVOR, DIGITE A OPÇÃO CORRETA! |')
    print('!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')

'''
███████╗███╗   ██╗████████╗██████╗  █████╗ ██████╗ 
██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
█████╗  ██╔██╗ ██║   ██║   ██████╔╝███████║██████╔╝
██╔══╝  ██║╚██╗██║   ██║   ██╔══██╗██╔══██║██╔══██╗
███████╗██║ ╚████║   ██║   ██║  ██║██║  ██║██║  ██║
╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
'''
def entrar():
    global usuario
    account_ok = 0
    password_ok = 0
    check_accounts()
    print('\n====================================')
    print('|          ENTRAR NO JOGO          |')
    print('====================================')
    usuario = input('\nDigite seu usuário: ')
    senha = input('Digite sua senha: ')

    for account in accounts:
        if usuario.lower() == account['username'].lower():
            account_ok = 1
            if senha == account['password']:
                password_ok = 1
                break

    if account_ok == 0:
        print('\n===================================================')
        print('| NÃO ENCONTRAMOS NENHUMA CONTA COM ESSE REGISTRO |')
        print('===================================================')
        menu()
    else:
        if password_ok == 0:
            print('\n=================================')
            print('| VOCÊ DIGITOU UMA SENHA ERRADA |')
            print('=================================')
            menu()
        else:
            game()

'''
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗██████╗  ██████╗ 
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   ██████╔╝██║   ██║
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══██╗██║   ██║
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
'''
def registro():
    while True:
        print('\n====================================')
        print('|             REGISTRO             |')
        print('====================================')
        check = 0

        check_accounts()

        usuario = input('\nDigite seu usuário: ')
        senha = input('Digite sua senha: ')

        if usuario != '':
            if senha != '':
                for account in accounts:
                    if usuario.lower() == account['username'].lower():
                        print('\nATENÇÃO! Usuário já registrado. Tente outro nome.\n')
                        check = 1

                if check == 0:
                    data_default_player['username'] = usuario
                    data_default_player['password'] = senha
                    accounts.append(data_default_player)

                    update_data()

                    print('\nRegistro realizado com sucesso!')
                    check_accounts()
                    menu()
                    break
                else:
                    menu()
                    break
            else:
                print('\n!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')
                print('| POR FAVOR, DIGITE UMA SENHA VÁLIDA! |')
                print('!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')
                menu()
                break
        else:
            print('\n!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')
            print('| !POR FAVOR, DIGITE UM USUÁRIO VÁLIDO! |')
            print('!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!=!')
            menu()
            break

'''
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗  
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
'''
def game():
    # Verificar se os dados estão ok.
    check_default()

    while True:
        opc = ''
        mult_equal = len(usuario)*'='
        print(f'\n======================================{mult_equal}')
        print(f'|  OLÁ {usuario.upper()}, ESCOLHA O QUE DESEJA FAZER  |')
        print(f'======================================{mult_equal}')
        print('''
    1 - Status
    2 - Procurar batalha
    3 - Sair
        ''')
        opc = input('Escolha uma das opções: ')
        try:
            if int(opc) == 1:
                status_player()
            elif int(opc) == 2:
                search_battle()
                break
            elif int(opc) == 3:
                menu()
                break
            else:
                error_menu()
        
        except ValueError as err: 
            error_menu()

'''
███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
'''
def status_player():
    print('\n===================================')
    print('|    STATUS DO SEU PERSONAGEM!    |')
    print('===================================\n')

    read_accounts()
    for account in accounts:
        if usuario.lower() == account['username'].lower():
            for k, v in account.items():
                print(f'{k}: {v}')
            break

'''
███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
███████╗█████╗  ███████║██████╔╝██║     ███████║    ██████╔╝███████║   ██║      ██║   ██║     █████╗  
╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║    ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
'''
def search_battle():
    global enemy
    enemy = choice(read_enemies())

    mult_equal = (len(enemy['pre3'])+len(enemy['name'])+len(str(enemy['health'])))*'='
    print(f'\n===================================={mult_equal}')
    print(f'|  VOCÊ ENCONTROU {enemy["pre3"].upper()} {enemy["name"].upper()} COM {enemy["health"]} DE VIDA!  |')
    print(f'===================================={mult_equal}')

    while True:
        fight = input('\nDeseja continuar com esta batalha? (S para sim ou N para não): ')
        try:
            if fight.upper() == 'S':
                battle()
                break
            elif fight.upper() == 'N':
                game()
                break
            else:
                error_menu()

        except ValueError as err: 
            error_menu()

'''
██████╗ ███████╗ █████╗ ██████╗     ███████╗███╗   ██╗███████╗███╗   ███╗██╗███████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔════╝████╗ ████║██║██╔════╝██╔════╝
██████╔╝█████╗  ███████║██║  ██║    █████╗  ██╔██╗ ██║█████╗  ██╔████╔██║██║█████╗  ███████╗
██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║██╔══╝  ╚════██║
██║  ██║███████╗██║  ██║██████╔╝    ███████╗██║ ╚████║███████╗██║ ╚═╝ ██║██║███████╗███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝
'''
def read_enemies():
    global enemies
    while True:
        try:
            if stat(enemies_file).st_size == 0:
                enemies_list = []
                enemies_list.append(data_default_enemy)
                with open(enemies_file, 'w', encoding='utf-8') as enemies_l:
                    dump(enemies_list, enemies_l, indent=4, separators=(',', ': '))
                break
            else:
                break

        except FileNotFoundError as err:
            print(f'Error: {err}')
            enemies_list = []
            enemies_list.append(data_default_enemy)
            with open(enemies_file, 'w', encoding='utf-8') as enemies_l:
                dump(enemies_list, enemies_l, indent=4, separators=(',', ': '))
            print(f'File {enemies_file} created!')
            break

    with open(enemies_file, encoding='utf-8') as en:
        enemies = load(en)

    return enemies

'''
██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██████╔╝███████║   ██║      ██║   ██║     █████╗  
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
'''
def battle():
    enemy_dead = 0
    # ADAPTAR SORTEIO PARA QUEM ATACA PRIMEIRO
    # POR ENQUANTO O PLAYER ESTÁ COMEÇANDO O ATAQUE
    # turn = ['enemy', 'player']
    # if turn[randrange(len(turn))] == 'player':
    read_accounts()
    while int(enemy['health']) > 0:
        for account in accounts:
            if usuario.lower() == account['username'].lower():
                player_health = int(account['health'])
                player_healthMax = int(account['healthMax'])
                player_exp = int(account['exp'])
                player_atkMin = int(account['atkMin'])
                player_atkMax = int(account['atkMax'])
                player_dmg = randint(player_atkMin, player_atkMax)
                enemy_health = int(enemy['health'])
                enemy_new_health = enemy_health - player_dmg
                enemy_exp = int(enemy['exp'])
                enemy_atk = int(enemy['atk'])
                print(f'\n============================================================')
                if enemy_new_health <= 0:
                    enemy_new_health = 0
                    print(f'Seu último dano {enemy["pre1"]} {enemy["name"]} foi {player_dmg} e você {enemy["pre2"]} matou!')
                    print(f'VOCÊ GANHOU {enemy_exp} DE EXPERIÊNCIA E SUA VIDA FOI RESTAURADA.')
                    account['health'] = player_healthMax
                    account['exp'] = player_exp + enemy_exp
                    enemy_dead = 1
                else:
                    print(f'Seu dano {enemy["pre1"]} {enemy["name"]} foi {player_dmg} e {enemy["pre2"]} deixou com {enemy_new_health} de vida.')
                    enemy['health'] = enemy_new_health

                if enemy_dead == 0:
                    player_new_health = player_health - enemy_atk
                    account['health'] = player_new_health
                    print(f'{enemy["pre2"].upper()} {enemy["name"]} te deu um dano de {enemy_atk}. Sua vida era {player_health} e passou a ser {player_new_health}.')
                print(f'============================================================')
                
                update_data()
                read_accounts()

        if enemy_dead:
            game()
            break

'''
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗     █████╗  ██████╗ ██████╗
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    ██╔══██╗██╔════╝██╔════╝
██║     ███████║█████╗  ██║     █████╔╝     ███████║██║     ██║     
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     ██╔══██║██║     ██║     
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    ██║  ██║╚██████╗╚██████╗
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
'''
def check_accounts():
    while True:
        try:
            if stat(accounts_file).st_size == 0:
                with open(accounts_file, 'w') as arq:
                    arq.write('[]')
            else:
                read_accounts()

                # Apenas para ajudar no desenvolvimento.
                print('\n========INFORMAÇÃO PROVISÓRIA========')
                account_list = []
                for account in read_accounts():
                    account_list.append(account['username'])
                print(f'Total de account(s) registrada(s): {len(account_list)}\nAccount(s): {account_list}')
                print('=====================================')
                # Apenas para ajudar no desenvolvimento.

                break

        except FileNotFoundError as err:
            print(f'Error: {err}')
            with open(accounts_file, 'w') as arq:
                arq.write('[]')
                print(f'File {accounts_file} created!')

'''
██████╗ ███████╗ █████╗ ██████╗      █████╗  ██████╗ ██████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔════╝
██████╔╝█████╗  ███████║██║  ██║    ███████║██║     ██║     
██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██╔══██║██║     ██║     
██║  ██║███████╗██║  ██║██████╔╝    ██║  ██║╚██████╗╚██████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝
'''
def read_accounts():
    global accounts
    with open(accounts_file, encoding='utf-8') as acc:
        accounts = load(acc)

    return accounts

'''
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗    ██████╗  █████╗ ████████╗ █████╗ 
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗      ██║  ██║███████║   ██║   ███████║
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝      ██║  ██║██╔══██║   ██║   ██╔══██║
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗    ██████╔╝██║  ██║   ██║   ██║  ██║
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
'''
def update_data():
    with open(accounts_file, 'w', encoding='utf-8') as acc:
        dump(accounts, acc, indent=4, separators=(',', ': '))

'''
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    ██████╗ ███████╗███████╗ █████╗ ██╗   ██╗██╗  ████████╗
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    ██╔══██╗██╔════╝██╔════╝██╔══██╗██║   ██║██║  ╚══██╔══╝
██║     ███████║█████╗  ██║     █████╔╝     ██║  ██║█████╗  █████╗  ███████║██║   ██║██║     ██║   
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     ██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║   ██║██║     ██║   
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    ██████╔╝███████╗██║     ██║  ██║╚██████╔╝███████╗██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝   
'''
def check_default():
    cache = 0
    read_accounts()

    for k, v in data_default_player.items():
        for account in accounts:
            if usuario.lower() == account['username'].lower():
                if k not in account.keys():
                    account[k] = v
                    print(f'A chave "{k}" com o valor "{v}" foi adicionado.')
                    cache = 1

    if cache:
        update_data()
        print('Dados Default foram atualizados.\n')


introducao()
