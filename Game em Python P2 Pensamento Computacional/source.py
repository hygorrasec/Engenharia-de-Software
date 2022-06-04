"""
Curso: Engenharia de Software
Período: 1o
Disciplina: Pensamento Computacional
Grupo: Fabrício Souza, Hygor Rasec e Victor Bernardo
Tema escolhido: Game em Python no estilo RPG.
Versão: 1.5
"""

dados = []


def login():
    check = 0
    print('LOGIN:\n')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    for i in dados:
        if email == i[0]:
            if senha == i[1]:
                print(f'\nVOCÊ LOGOU COM O EMAIL "{email}"!')
                print('Estamos em construção, volte em breve para conhecer o nosso jogo!')
                print('Até logo!\n')
                check = 1
                break
    if check == 0:
        print('\nNão encontramos nenhuma conta com esse registro.\n')
        menu()


def registro():
    while True:
        print('REGISTRO:\n')
        check = 0
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        if email != '':
            if senha != '':
                for i in dados:
                    if email == i[0]:
                        print('\nE-mail já registrado.\n')
                        check = 1
                        break

                if check == 0:
                    dados.append([email, senha])
                    print('\nRegistro realizado com sucesso!\n')
                    print(f'Registros: {dados}\n')
                    menu()
                    break
                else:
                    menu()
                    break
            else:
                print('\nPor favor, digite uma senha válida.\n')
        else:
            print('\nPor favor, digite um email válido.\n')


def menu():
    while True:
        print("""Digite um número de acordo com o que deseja fazer:

    1 - Login
    2 - Criar uma nova conta
    3 - Sair
        """)
        opc = input('Escolha uma das opções: ')
        try:
            print('')
            if int(opc) == 1:
                login()
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
Se você já tem uma jornada, digite 1 para logar. Caso seja um novo aventureiro, digite 2 para criar sua conta ou digite 3 para sair.
       """)
    menu()


introducao()
