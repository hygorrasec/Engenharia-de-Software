"""
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

"""

from random import choice, randrange, randint
from json import dump, load
from os import stat

accounts_file = 'accounts.json'
enemies_file = 'enemies.json'
data_default = {
                    'username': '',
                    'password': '',
                    'level': 1,
                    'health': 100,
                    'exp': 0,
                    'first': 1,
                    'atkMin': 10,
                    'atkMax': 20,
                    'healthPotion': 1000
                }


"""
██╗███╗   ██╗████████╗██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗ █████╗  ██████╗ 
██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝██╔══██╗██╔═══██╗
██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║██║   ██║██║     ███████║██║   ██║
██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██║   ██║██║     ██╔══██║██║   ██║
██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗██║  ██║╚██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝                                                                                
"""
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
    print('ENTRAR:\n')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

    check_accounts()

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
        print('REGISTRO:\n')
        check = 0

        check_accounts()

        usuario = input('Digite seu usuário: ')
        senha = input('Digite sua senha: ')

        if usuario != '':
            if senha != '':
                for account in accounts:
                    if usuario.lower() == account['username'].lower():
                        print('\nATENÇÃO! Usuário já registrado. Tente outro nome.\n')
                        check = 1

                if check == 0:
                    data_default['username'] = usuario
                    data_default['password'] = senha
                    accounts.append(data_default)

                    with open(accounts_file, "w", encoding="utf-8") as acc:
                        dump(accounts, acc, indent=4, separators=(",", ": ")) 

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
                menu()
                break
        
        except ValueError as err: 
            if opc != 1 or opc != 2 or opc != 3 or err:
                print('Por favor digite apenas os numeros apresentados no menu.\n')

'''
███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
███████╗   ██║   ███████║   ██║   ██║   ██║███████╗    ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║    ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
'''
def status_player():
    print('Status do seu personagem:')
    print('=========================')

    read_accounts()
    for account in accounts:
        if usuario.lower() == account['username'].lower():
            for k, v in account.items():
                print(f'{k}: {v}')
            break

    print('')

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

    print(f'Você acabou de encontrar {enemy["pre3"]} {enemy["name"]} com {enemy["health"]} de vida!')
    print(f'=========================================\n')

    fight = input('Deseja continuar com esta batalha? (S para sim ou N para não): ')
    try:
        print('')
        if fight.upper() == 'S':
            battle()
        elif fight.upper() == 'N':
            game()
    
    except ValueError as err: 
        if fight.upper() != 'N' or fight.upper() != 'S' or err:
            print('Por favor digite apenas as letras apresentadas no menu.\n')

'''
██████╗ ███████╗ █████╗ ██████╗     ███████╗███╗   ██╗███████╗███╗   ███╗██╗███████╗███████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔════╝████╗  ██║██╔════╝████╗ ████║██║██╔════╝██╔════╝
██████╔╝█████╗  ███████║██║  ██║    █████╗  ██╔██╗ ██║█████╗  ██╔████╔██║██║█████╗  ███████╗
██╔══██╗██╔══╝  ██╔══██║██║  ██║    ██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║██╔══╝  ╚════██║
██║  ██║███████╗██║  ██║██████╔╝    ███████╗██║ ╚████║███████╗██║ ╚═╝ ██║██║███████╗███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝
'''
def read_enemies():
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
    while int(enemy["health"]) > 0:
        for account in accounts:
            if usuario.lower() == account['username'].lower():
                player_health = account['health']
                player_exp = account['exp']
                player_atkMin = account['atkMin']
                player_atkMax = account['atkMax']
                player_dmg = randint(int(player_atkMin), int(player_atkMax))
                enemy_new_health = int(enemy["health"]) - int(player_dmg)
                print(f'============================================================')
                if enemy_new_health <= 0:
                    enemy_new_health = 0
                    print(f'Seu dano {enemy["pre1"]} {enemy["name"]} foi {player_dmg} e você {enemy["pre2"]} matou.')
                    print(f'Você ganhou {int(enemy["exp"])} de experiência.')
                    enemy_dead = 1
                else:
                    print(f'Seu dano {enemy["pre1"]} {enemy["name"]} foi {player_dmg} e {enemy["pre2"]} deixou com {enemy_new_health} de vida.')

                player_new_health = int(player_health) - int(enemy['atk'])
                player_new_exp = int(player_exp) + int(enemy["exp"])

                if enemy_dead == 0:
                    print(f'{enemy["pre2"].upper()} {enemy["name"]} te deu um dano de {int(enemy["atk"])}. Sua vida era {player_health} e passou a ser {player_new_health}.')
                print(f'============================================================\n')

                account['health'] = player_new_health
                account['exp'] = player_new_exp
                enemy["health"] = enemy_new_health
                
                update_data()
                read_accounts()

                with open(accounts_file, "w", encoding="utf-8") as acc:
                    dump(accounts, acc, indent=4, separators=(",", ": ")) 

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
                print('')
                print('=======================================')
                account_list = []
                for account in read_accounts():
                    account_list.append(account['username'])
                print(f'Total de account(s) registrada(s): {len(account_list)}\nAccount(s): {account_list}')
                print('=======================================')
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
    with open(accounts_file, "w", encoding="utf-8") as acc:
        dump(accounts, acc, indent=4, separators=(",", ": "))

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

    for k, v in data_default.items():
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
