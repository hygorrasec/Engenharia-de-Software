"""
Curso: Engenharia de Software
Período: 1o
Disciplina: Pensamento Computacional
Grupo: Fabrício Souza, Hygor Rasec e Victor Bernardo
Tema escolhido: Game em Python no estilo RPG.
Versão: 1.6

====================================================

INFORMAÇÕES IMPORTANTES PARA FINS DE ESTUDO:

# os.listdir() -> Listando arquivos e diretórios
# os.chdir() -> Muda o diretório.
# os.getcwd() -> Retorna o caminho absoludo.
# os.path.join() -> Recebe dois parâmetros, sendo o primeiro diretório atual e o segundo o diretório que será juntado ao atual.

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

def entrar():
    global password_ok
    account_ok = 0
    password_ok = 0
    print('ENTRAR:\n')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')

    for account in os.listdir('accounts'):
        if usuario == account.split(extension_data)[0]:
            account_ok = 1

            os.chdir(os.path.join(os.getcwd(), 'accounts'))
            with open(account) as arquivo:
                if senha == arquivo.read().split(',')[1]:
                    print(f'\nVOCÊ ENTROU COM O USUÁRIO: "{usuario}"!')
                    print('Estamos em construção, volte em breve para conhecer o nosso jogo!')
                    print('Até logo!\n')
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


def check_accounts():
    accounts = []
    
    # Adicionada em uma lista provisória os usuários sem a extensão .txt
    for account in os.listdir('accounts'):
        accounts.append(account.split(extension_data)[0])

    print(f'Total de accounts registradas: {len(accounts)}\nAccounts: {accounts}\n')


def registro():
    while True:
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
                        arquivo.write(f'{usuario},{senha}')
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
    print("""
Olá, jogador! Seja bem-vindo ao Delta AVA Game! Vamos iniciar sua jornada...
Se você já tem uma jornada, digite 1 para entrar. Caso seja um novo aventureiro, digite 2 para criar sua conta ou digite 3 para sair.
       """)
    menu()


introducao()
