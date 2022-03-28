# Variáveis
version = 1.0
dev = "Hygor Rasec"
whatsapp = "21 99724-8557"
email = "hygorrasec@gmail.com"

cm = 1 # 1 centímetro (cm)
m = 100 # 1 metro (m) = 100 centímetros (cm)
km = 100000 # 1 quilômtro (km) = 100000 centímetros (cm)

mile = 160934.4 # 1 milha (mile – mi) = 160934.4 centímetro (cm)
inch = 2.54 # 1 polegada (inch – in) = 2,54 centímetro (cm)
foot = 30.48 # 1 pé (foot – ft) = 30,48 centímetro (cm)

print("========================================================================")
print(f"====PROGRAMA DE CONVERSÃO DE MEDIDAS - DESENVOLVIDO POR {dev}====")
print("========================================================================\n")

# Primeiro Input
while True:
    unidade_medida = input("Digite o número correspondente a Unidade de Medida que deseja converter:\n\n(1) = Milhas\n(2) = Polegadas\n(3) = Pés\n(4) = Centímetros\n(5) = Metros\n(6) = Quilômetros\n\nDigite aqui: ")
    if (unidade_medida.isnumeric()) and (int(unidade_medida) >= 1) and (int(unidade_medida) <= 6):
        break
    else:
        print(f"\nVocê digitou: '{unidade_medida}'. Por favor, digite um dos números que estão na lista apresentada!\n")

# Função que Checa o Input
def check_input(medida):
    while True:
        quantidade = input(f"\nVocê escolheu a opção '{medida}'. Agora precisamos saber o valor (em número) que você deseja converter.\n\nDigite aqui: ")
        if (quantidade.isnumeric()):
            break
        else:
            print(f"\nVocê digitou: '{quantidade}'. Por favor, insira um número válido.")

    return quantidade

# Função do Resultado Final
def result(medida_escolhida,medida):
    quantidade = float(check_input(medida_escolhida))
    qnt_formatado = "{:.0f}".format(quantidade)
    medidas = ["milha", "polegada", "pé", "centímetro", "metro", "quilômetro"]
    calc = [mile, inch, foot, cm, m, km]

    print(f"\nSegue abaixo as Conversões de Medidas do valor {qnt_formatado} que você escolheu:\n")

    count = 0
    for c1 in calc:
        c2 = "{:.6f}".format((quantidade*medida)/c1)
        print(f"{qnt_formatado} {medida_escolhida}(s) = {c2} {medidas[count]}(s)")
        count += 1

match int(unidade_medida):
    case 1:
        result("Milha",mile)
    case 2:
        result("Polegada",inch)
    case 3:
        result("Pé",foot)
    case 4:
        result("Centímetro",cm)
    case 5:
        result("Metro",m)
    case 6:
        result("Quilômetro",km)

print("\n=============FIM=============\n")
input(f"Versão do Programa: {version}\nDev.: {dev}\nContato(Whatsapp): {whatsapp}\nEmail: {email}\n\nObrigado por usar o meu programa!\n\nPressione alguma tecla para fechar.")
