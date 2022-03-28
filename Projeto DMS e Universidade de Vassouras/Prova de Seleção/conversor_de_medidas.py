# Variáveis
version = 1.0
dev = "Hygor Rasec"
whatsapp = "21 99724-8557"
email = "hygorrasec@gmail.com"

medidas = ["Milha", "Polegada", "Pé", "Centímetro", "Metro", "Quilômetro"]
calc = [160934.4, 2.54, 30.48, 1, 100, 100000]

print("========================================================================")
print(f"====PROGRAMA DE CONVERSÃO DE MEDIDAS - DESENVOLVIDO POR {dev}====")
print("========================================================================\n")

# Primeiro Input
while True:
    unidade_medida = input("Digite o número correspondente a Unidade de Medida que deseja converter:\n\n(0) = Milha\n(1) = Polegada\n(2) = Pé\n(3) = Centímetro\n(4) = Metro\n(5) = Quilômetro\n\nDigite aqui: ")
    if (unidade_medida.isnumeric()) and (int(unidade_medida) >= 0) and (int(unidade_medida) <= 5):
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
def result(medida_escolhida,medida,unidade_medida):
    quantidade = float(check_input(medida_escolhida))
    qnt_formatado = "{:.0f}".format(quantidade)

    print(f"\nSegue abaixo as Conversões de Medidas do valor {qnt_formatado} que você escolheu:\n")

    count = 0
    for c1 in calc:
        c2 = "{:.6f}".format((quantidade*medida)/c1)
        print(f"{qnt_formatado} {medidas[unidade_medida]}(s) = {c2} {medidas[count]}(s)")
        count += 1

result(medidas[int(unidade_medida)],calc[int(unidade_medida)],int(unidade_medida))

print("\n=============FIM=============\n")
input(f"Versão do Programa: {version}\nDev.: {dev}\nContato(Whatsapp): {whatsapp}\nEmail: {email}\n\nObrigado por usar o meu programa!\n\nPressione alguma tecla para fechar.")
