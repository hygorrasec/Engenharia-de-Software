"""
Curso: Engenharia de Software
Período: 1o
Disciplina: Pensamento Computacional
Grupo: Fabrício Souza, Hygor Rasec e Victor Bernardo
Tema escolhido: Game em Python no estilo RPG.
Versão: 1.7

====================================================

INFORMAÇÕES IMPORTANTES PARA FINS DE ESTUDO:

# os.listdir() -> Listando arquivos e diretórios
# os.chdir() -> Muda o diretório.
# os.getcwd() -> Retorna o caminho absoludo.
# os.path.join() -> Recebe dois parâmetros, sendo o primeiro diretório atual e o segundo o diretório que será juntado ao atual.
# eval() -> Converte string em formato de lista para uma lista real.

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
import os

extension_data = '.txt'
separator = ','
data_default = {'username': '', 'password': '', 'level': '1', 'health': '100', 'exp': '0', 'first': '1'}

def entrar():
    global usuario
    account_ok = 0
    password_ok = 0
    print('ENTRAR:\n')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

    try:
        for account in os.listdir('accounts'):
            if usuario == account.split(extension_data)[0]:
                account_ok = 1

                os.chdir(os.path.join(os.getcwd(), 'accounts'))
                with open(account) as arquivo:
                    user_account = eval(arquivo.read())
                    user_password = user_account.get('password')
                    user_username = user_account.get('username')
                    if senha == user_password:
                        print(f'\nVOCÊ ENTROU COM O USUÁRIO: {user_username}!\n')
                        password_ok = 1

                os.chdir('..')  # Voltar para o diretório raiz.  
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

    except FileNotFoundError as err:
        os.mkdir('accounts')
        print('\nNão encontramos nenhuma conta com esse registro.\n')
        menu()


def check_accounts():
    accounts = []
    
    # Adicionada em uma lista provisória os usuários sem a extensão .txt
    for account in os.listdir('accounts'):
        accounts.append(account.split(extension_data)[0])

    print(f'Total de accounts registradas: {len(accounts)}\nAccounts: {accounts}\n')


def registro():
    while True:
        try:
            print('REGISTRO:\n')
            check = 0

            check_accounts()

            usuario = input('Digite seu usuário: ')
            senha = input('Digite sua senha: ')
            if usuario != '':
                if senha != '':
                    for account in os.listdir('accounts'):
                        if usuario == account.split(extension_data)[0]:
                            print('\nUsuário já registrado.\n')
                            check = 1
                            break

                    if check == 0:
                        os.chdir(os.path.join(os.getcwd(), 'accounts'))  # Mudar para o diretório 'accounts'.
                        with open(usuario + extension_data, 'w') as arquivo:
                            data_default['username'] = usuario
                            data_default['password'] = senha
                            arquivo.write(f'{data_default}')

                        os.chdir('..')  # Voltar para o diretório raiz.
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
        except FileNotFoundError as err:
            os.mkdir('accounts')
        

def menu():
    while True:
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


def game():
    cache = 0
    # Verificar se os dados estão ok.
    for account in os.listdir('accounts'):
        if usuario == account.split(extension_data)[0]:
            os.chdir(os.path.join(os.getcwd(), 'accounts'))  # Mudar para o diretório 'accounts'.
            with open(account) as arquivo:
                user_account = eval(arquivo.read())
                user_username = user_account.get('username')

                for k, v in data_default.items():
                    if k not in user_account.keys():
                        user_account[k] = v
                        print(f'A chave "{k}" com o valor "{v}" foi adicionado.')
                        cache = 1

                if cache:
                    with open(usuario + extension_data, 'w') as arquivo:
                        arquivo.write(f'{user_account}')
                        print('Dados Default foram atualizados.\n')

            os.chdir('..')  # Voltar para o diretório raiz.

    print('Status do seu personagem:')
    print('=========================')
    for k, v in user_account.items():
        print(f'{k}: {v}')

    print('')
    while True:
        text = input(f'Player {user_username}, digite algo. Para sair, digite "sair": ')
        if text != 'sair':
            print(f'Você digitou: {text}\n')
        else:
            menu()
            break


introducao()
