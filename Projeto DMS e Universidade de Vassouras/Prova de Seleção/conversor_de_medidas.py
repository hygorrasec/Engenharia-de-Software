# Variáveis
version = 1.0
dev = "Hygor Rasec"
whatsapp = "21 99724-8557"
email = "hygorrasec@gmail.com"

medidas = {
    'Milha': 160934.4,
    'Polegada': 2.54,
    'Pé': 30.48,
    'Centímetro': 1,
    'Metro': 100,
    'Quilômetro': 100000
}

print("========================================================================")
print(f"====PROGRAMA DE CONVERSÃO DE MEDIDAS - DESENVOLVIDO POR {dev}====")
print("========================================================================\n")

# Primeiro Input
while True:
    unidade_medida = input("Digite o número correspondente a Unidade de Medida que deseja converter:\n\n(1) = Milha\n(2) = Polegada\n(3) = Pé\n(4) = Centímetro\n(5) = Metro\n(6) = Quilômetro\n\nDigite aqui: ")
    if (unidade_medida.isnumeric()) and (int(unidade_medida) > 0) and (int(unidade_medida) <= len(medidas)):
        count = 1
        for (key,value) in medidas.items():
            if count == int(unidade_medida):
                medida_escolhida = key
                valor_da_medida = value
                break
            else:
                count += 1
        break
    else:
        print(f"\nVocê digitou: '{unidade_medida}'. Por favor, digite um dos números que estão na lista apresentada!\n")

# Função que Checa o Input
def check_input(medida_escolhida):
    while True:
        quantidade = input(f"\nVocê escolheu a opção '{medida_escolhida}'. Agora precisamos saber o valor (em número) que você deseja converter.\n\nDigite aqui: ")
        if (quantidade.isnumeric()):
            break
        else:
            print(f"\nVocê digitou: '{quantidade}'. Por favor, insira um número válido.")

    return quantidade

# Função do Resultado Final
def result(medida_escolhida,valor_da_medida):
    quantidade = float(check_input(medida_escolhida))
    qnt_formatado = "{:.0f}".format(quantidade)

    print(f"\nSegue abaixo as Conversões de Medidas do valor {qnt_formatado} que você escolheu:\n")

    for (key,value) in medidas.items():
        c2 = "{:.6f}".format((quantidade*valor_da_medida)/value)
        print(f"{qnt_formatado} {medida_escolhida}(s) = {c2} {key}(s)")        

result(medida_escolhida,valor_da_medida)

print("\n=============FIM=============\n")
input(f"Versão do Programa: {version}\nDev.: {dev}\nContato(Whatsapp): {whatsapp}\nEmail: {email}\n\nObrigado por usar o meu programa!\n\nPressione alguma tecla para fechar.")
