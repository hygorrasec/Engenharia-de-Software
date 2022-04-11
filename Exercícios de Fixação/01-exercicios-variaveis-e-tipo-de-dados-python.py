"""
# 01 - Faça um programa que leia um número inteiro e o imprima.

numero_inteiro = int(5)
print(f'O número inteiro é: {numero_inteiro}')

# 02 - Faça um programa que leia um número real e o imprima.

numero_real = float(1.54)
print(f'O número real é: {numero_real}')

# 03 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
print(f'O resultado da soma ({n1} + {n2} + {n3}) foi: {n1+n2+n3}')

# 04 - Leia um número real e imprima o resultado do quadrado desse número.

numero_real = 1.74
ao_quadrado = numero_real*numero_real
print(f'O número {numero_real} elevado ao quadrado é: {ao_quadrado}')

# 05 - Leia um número real e imprima a quinta parte desse número.

numero_real = 1.12
quinta_parte = numero_real * 1/5
print(f'A quinta parte de {numero_real} é: {quinta_parte}')

# 06 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = C * 1.8 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

C = 10
F = C * 1.8 + 32
print(F'{C}º Celsius convertido em Fahrenheit é: {F}º Fahrenheit')

# 07 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = (F - 32) / 1.8, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.

F = 50
C = (F - 32) / 1.8
print(f'{F}º Fahrenheits convertido em Celsiu é: {C}º Celsiu')

# 08 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

K = 320
C = K - 273.15
print(f'{K}º Kelvin convertido em Celsiu é: {C}º Celsiu')

# 09 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é: K = C + 273.15, sendo K a temperatura em Kelvin e C a temperatura em Celsius.

C = 46
K = C + 273.15
print(f'{C}º Celsiu convertido em Kelvin é: {K}º Kelvin')

# 10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K / 3.6, sendo M a velocidade em m/s e K em km/h.

K = 72
M = K / 3.6
print(f'{K} km/h equivale a {M} m/s!')

# 11 - Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s.

M = 20
K = M * 3.6
print(f'{M} m/s equivale a {K} km/h!')
 
# 12 - Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = M * 0.62137, sendo K a distância em quilômetros e M em milhas.

M = 100
K = M / 0.62137
print(f'{M} milhas equivale a {K} quilômetros.')

# 13 - Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é: M = K / 0.62137, sendo M a distância em milhas e K em quilômetros.

K = 160
M = K * 0.62137
print(f'{K} quilômetros equivale a {M} milhas.')

# 14 - Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * pi / 180, sendo G o ângulo em graus e R em radianos e pi = 3.141592653589793

import math

G = 50
R = G * math.pi / 180
print(f'{G} graus em radianos fica: {R} rad')

# 15 - Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R * 180 / pi, sendo R o ângulo em radianos e G em graus e pi = 3.141592653589793

import math

R = 1
G = R * 180 / math.pi
print(f'{R} radianos em graus fica: {G} graus')

# 16 - Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão é: C = P / 0.39370, sendo C o comprimento em centímetros e P o comprimento em polegadas.

P = 30
C = P / 0.39370
print(f'{P} polegadas é o mesmo que {C} centímetros!')

# 17 - Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de conversão é: P = C * 0.39370, sendo P o comprimento em polegadas e C o comprimento em centímetros.

C = 100
P = C * 0.39370
print(f'{C} centímetros é o mesmo que {P} polegadas!')

# 18 - Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é: L = M / 0.0010000, sendo L o volume em litros e M o volume em metros cúbicos.

M = 20
L = M / 0.0010000
print(f'{M} m³ possui {L} litros.')

# 19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A fórmula de conversão é: M = L * 0.0010000, sendo M o volume em metros cúbicos e L o volume em litros.

L = 20000
M = L * 0.0010000
print(f'{L} litros possui {M} m³.')

# 20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é: L = K * 2.2046, sendo L a massa em libras e K a massa em quilogramas.

K = 85
L = K * 2.2046
print(f'{K} quilogramas tem {L} libras.')

# 21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L / 2.2046, sendo K a massa em quilogramas e L a massa em libras.

L = 187
K = L / 2.2046
print(f'{L} libras tem {K} quilogramas.')

# 22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = J / 1.0936, sendo M o comprimento em metros e J o comprimento em jardas.

J = 20
M = J / 1.0936
print(f'{J} jardas tem {M} metros.')

# 23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é: J = M * 1.0936, sendo J o comprimento em jardas e M o comprimento em metros.

M = 20
J = M * 1.0936
print(f'{M} metros tem {J} jardas.')

# 24 - Leia um valor de área em m² (metros quadrados) e apresente-o convertido em acres. A fórmula de conversão é: A = M * 0.00024711, sendo A a área em acres e M a área em metros quadrados.

M = 10
A = M * 0.00024711
print(f'{M} m² tem {A} acres.')

# 25 - Leia um valor de área em acres e apresente-o convertido em m² (metros quadrados). A fórmula de conversão é: M = A / 0.00024711, sendo M a área em metros quadrados e A a área em acres.

A = 1
M = A / 0.00024711
print(f'{A} acres tem {M} m².')

# 26 - Leia um valor de área em m² (metros quadrados) e apresente-o convertido em hectares. A fórmula de conversão é: H = M / 10000, sendo H a área em hectares e M a área em metros quadrados.

M = 20
H = M / 10000
print(f'{M} m² tem {H} hectares.')

# 27 - Leia um valor de área em hectares e apresente-o convertido em m² (metros quadrados). A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.

H = 1
M = H * 10000
print(f'{H} hectares tem {M} m².')

# 28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.

v1, v2, v3 = 5, 4, 2
print(f'A soma dos quadrados dos três valores ({v1} + {v2} + {v3}) são: ({v1*v1} + {v2*v2} + {v3*v3}) = {v1*v1+v2*v2+v3*v3}')

# 29 - Leia quatro notas, calcule a média aritmética e imprima o resultado.

n1, n2, n3, n4 = 8, 7, 7, 8
media = (n1+n2+n3+n4)/4
print(f'A média aritmética das notas foi: {media}')

# 30 - Leia um valor em real e a cotação em dólar. Em seguida, imprima o valor correspondente em dólares.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8") # Definindo localização da moeda para pt-BR

real = 2
real_locale = locale.currency(real, grouping=True)

locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8") # Alterando localização da moeda para en_US
cotacao_dolar = 4.70

print(f'{real_locale} está custando hoje {locale.currency(cotacao_dolar*real, grouping=True)} dólares.')

# 31 - Leia um número inteiro e imprima o seu antecessor e o seu sucessor.

numero = 0
antecessor = numero-1
sucessor = numero+1
print(f'O número {numero} tem como antecessor o número {antecessor} e como sucessor o número {sucessor}.')

# 32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

n = 5
n_triplo_sucessor = n*3+1
n_dobro_antecessor = n*2-1
soma = n_triplo_sucessor+n_dobro_antecessor
print(f'A soma do sucessor do triplo de {n} ({n_triplo_sucessor}) mais o antecessor do dobro de {n} ({n_dobro_antecessor}) resulta em: {soma}.')

# 33 - Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.

l = 1.5
a = l*l
print(f'A área do quadrado com lado de {l}m tem {a}m².')

# 34 - Leia o valor do raio de um círculo, calcule e imprima a área do círculo correspondente. A área do círculo é raio² * pi, considerando pi = 3.141592653589793.

import math

raio = 3
a = (raio*raio) * math.pi
print(f'A área do círculo com raio {raio} cm tem {a} cm².')

# 35 - Seja 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raiz de (a² + b²). Faça um programa que receba os valores de 'a' e 'b' e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.

import math

cateto_a = 5
cateto_b = 7
soma_catetos = (cateto_a*cateto_a)+(cateto_b*cateto_b)
raiz = math.sqrt(soma_catetos)
print(f'A soma dos quadrados dos catetos {cateto_a} e {cateto_b} de um triângulo retângulo é igual a {raiz}')

# 36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio² * altura, onde pi = 3.141592653589793.

import math

altura = 5
raio = 4
volume = math.pi * (raio*raio) * altura
print(f'Um cilindro circular com altura {altura} cm e raio {raio} cm tem volume de {volume} cm³.')

# 37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

valor = 80
desconto_porcentagem = 12
total = locale.currency(valor*((100-desconto_porcentagem)/100), grouping=True)
print(f'O procuto custa {locale.currency(valor, grouping=True)} e com desconto de {desconto_porcentagem}% passa a ser {total}.')

# 38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

salario = 1200
aumento_porcentagem = 25
novo_salario = locale.currency(salario*((aumento_porcentagem/100)+1), grouping=True)
print(f'O funcionário recebia {locale.currency(salario, grouping=True)}. Com aumento de {aumento_porcentagem}%, seu salário foi para {novo_salario}.')

# 39 - A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# -> O primeiro colocado receberá 46%;
# -> O segundo colocado receberá 32%;
# -> O terceiro colocado receberá o restante;

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

premiacao_total = 780000
primeiro_lugar = 46
segundo_lugar = 32
terceiro_lugar = 100-primeiro_lugar-segundo_lugar
valor_primeiro = locale.currency(premiacao_total*(primeiro_lugar/100), grouping=True)
valor_segundo = locale.currency(premiacao_total*(segundo_lugar/100), grouping=True)
valor_terceiro = locale.currency(premiacao_total*(terceiro_lugar/100), grouping=True)

print(f'O primeiro colocado ganhou {valor_primeiro}.\nO segundo colocado ganhou {valor_segundo}.\nO terceiro colocado ganhou {valor_terceiro}.')

# 40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhos pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

custo_dia = 30
dias_trabalhados = int(input('Quantos dias o encanador trabalhou? '))
total_custo_dia = custo_dia*dias_trabalhados
desconto_IR_porcentagem = 8
total_a_pagar = locale.currency(total_custo_dia*((100-desconto_IR_porcentagem)/100), grouping=True)

print(f'O contrato do encanador custa {locale.currency(custo_dia, grouping=True)} à diária. O mesmo trabalhou {dias_trabalhados} dia(s) e vai receber o valor de {total_a_pagar} incluindo o desconto de {desconto_IR_porcentagem}% referente ao importo de renda.')

# 41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

valor_hora = 20
horas_trabalhas = 220
adicional_porcentagem = 10
total_a_pagar = locale.currency((valor_hora*horas_trabalhas)*((adicional_porcentagem/100)+1), grouping=True)
print(f'O valor da hora de trabalho é de {locale.currency(valor_hora, grouping=True)}. O funcionário trabalhou {horas_trabalhas} horas no mês e vai receber um sálário de {total_a_pagar} já incluso os {adicional_porcentagem}% sobre o valor.')

# 42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de importo sobre o salário-base.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

salario_base = 1200
gratificacao_porcentagem = 5
salario_base_gratificacao = salario_base*((gratificacao_porcentagem/100)+1)
imposto_porcentagem = 7
imposto = salario_base*((imposto_porcentagem)/100)
total_a_receber = locale.currency(salario_base_gratificacao-imposto, grouping=True)
print(f'O salário-base do funcionário é de {locale.currency(salario_base, grouping=True)}. Ele recebeu uma gratificação de {gratificacao_porcentagem}% sobre o salário-base e paga {imposto_porcentagem}% de importo sobre o salário-base. Seu salário a receber será de {total_a_receber}.')

# 43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# -> O total a pagar com desconto de 10%;
# -> O valor de cada parcela, no parcelamento de 3x sem juros;
# -> A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
# -> A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

valor_produto = 100
desconto_porcentagem_a_vista = 10
valor_produto_desconto = valor_produto*((100-desconto_porcentagem_a_vista)/100)
numero_parcelas = 3
parcelas_3x_sem_juros = valor_produto/numero_parcelas
comissao_a_vista_porcentagem = 5
comissao_a_vista = valor_produto_desconto*(comissao_a_vista_porcentagem/100)
comissao_parcela_porcentagem = 5
comissao_parcela = valor_produto*(comissao_parcela_porcentagem/100)

print(f'O produto custa {locale.currency(valor_produto, grouping=True)}.\nSe o pagamento for à vista, terá um desconto de {comissao_a_vista_porcentagem}% e pagará {locale.currency(valor_produto_desconto, grouping=True)}.\nTambém poderá parcelar em {numero_parcelas}x de {locale.currency(parcelas_3x_sem_juros, grouping=True)} (sem juros).\nO vendedor ganhará comissão de {comissao_a_vista_porcentagem}% sobre o valor do produto com desconto, caso o pagamento seja a vista. Ou seja, o produto saindo por {locale.currency(valor_produto_desconto, grouping=True)}, o vendedor ganhará {locale.currency(comissao_a_vista, grouping=True)}.\nSe houver parcelamento, o vendedor ganhará comissão de {comissao_parcela_porcentagem}% sobre o valor total. Ou seja, o produto custando {locale.currency(valor_produto, grouping=True)}, o vendedor ganhará {locale.currency(comissao_parcela, grouping=True)}.')

# 44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

altura_degrau_cm = 20
algura_destino_cm = 200
algura_destino_m = int(algura_destino_cm/100)
degraus_necessarios = int(algura_destino_cm/altura_degrau_cm)
print(f'Cada degrau de uma escada possui {altura_degrau_cm}cm de afastamento e o usuário precisa subir {algura_destino_m} metro(s). Sendo assim, o usuário deverá subir {degraus_necessarios} degraus para atindir seu objetivo.')

# 45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.

letra_maiuscula = 'U'
letra_minuscula = letra_maiuscula.lower()
print(f'A letra maiúscula é "{letra_maiuscula}" e convertendo para minúscula fica "{letra_minuscula}".')


# 46 - Faça um programa que leia um número inteiro positivo de três digitos (de 100 a 999). Gere outro número formado pelos digitos invertidos do número lido. Exemplo:
# numero_lido = 123
# numero_gerado = 321

numero_lido = 456
numero_lido_para_str = str(numero_lido)
numero_gerado = numero_lido_para_str[::-1]
print(f'O número lido foi {numero_lido}. Esse número invertido fica {numero_gerado}.')

# 47 - Leia um número inteiro de 4 digitos (de 1000 a 9999) e imprima 1 dígito por linha.

numero_inteiro = 4567
numero_inteiro_para_str = str(numero_inteiro)
print(f'{numero_inteiro_para_str[0]}\n{numero_inteiro_para_str[1]}\n{numero_inteiro_para_str[2]}\n{numero_inteiro_para_str[3]}')

# 48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos = 12345
segundos = segundos % (24 * 3600) 
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f'{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)')

# 49 - Faça um programa que leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de um experiência biológico. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma.

inicio_hora, inicio_minuto, inicio_segundo = 2, 20, 30

hora_segundos = inicio_hora * 3600
minuto_segundo = inicio_minuto * 60
segundos_inicial_soma = hora_segundos+minuto_segundo+inicio_segundo

segundos_inicial = segundos_inicial_soma % (24 * 3600) 
horas = segundos_inicial // 3600
segundos_inicial %= 3600
minutos = segundos_inicial // 60
segundos_inicial %= 60

duracao_em_segundos = 7000
total_segundos = segundos_inicial_soma+duracao_em_segundos

total_segundos = total_segundos % (24 * 3600) 
horas_final = total_segundos // 3600
total_segundos %= 3600
minutos_final = total_segundos // 60
total_segundos %= 60

print(f'A experiência biológico começou às {inicio_hora} hora(s), {inicio_minuto} minuto(s) e {inicio_segundo} segundo(s) e durou {duracao_em_segundos} segundos.\nA experiência biológico então terminou às {horas_final} hora(s), {minutos_final} minuto(s) e {total_segundos} segundo(s).')

# 50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

idade = 34
ano_atual = 2022
ano_nascimento = ano_atual-idade
print(f'Você tem {idade} anos então nasceu em {ano_nascimento}.')

# 51 - Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0;0).

import math

Ax, Ay, Bx, By = 2, 3, 0, 0

x = Ax-Bx
y = Ay-By
x = x*x
y = y*y
d = str(math.sqrt(x+y))[0:4]
print(f'Com a coordenada x = {Ax}cm e y = {Ay}cm temos o ponto A.\nA distância entre o ponto A e o ponto B (0;0) é de {d}cm.')

# 52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

premio = 1_000_000
amigo01, amigo02, amigo03 = 15, 35, 25

apostaTotal = amigo01 + amigo02 + amigo03
p1 = premio*(amigo01/apostaTotal)
p2 = premio*(amigo02/apostaTotal)
p3 = premio*(amigo03/apostaTotal)

print(f'O amigo 1 apostou: {locale.currency(amigo01, grouping=True)}\nO amigo 2 apostou: {locale.currency(amigo02, grouping=True)}\nO amigo 3 apostou: {locale.currency(amigo03, grouping=True)}\n\nO amigo 1 recebe: {locale.currency(p1, grouping=True)}\nO amigo 2 recebe: {locale.currency(p2, grouping=True)}\nO amigo 3 recebe: {locale.currency(p3, grouping=True)}')

# EXTRA 01 - Faça um programa que receba um emoji de coração.

coracao = chr(3)
print(coracao)

# 53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.

import locale
locale.setlocale(locale.LC_MONETARY, "pt-BR.UTF-8")

c = 10
l = 12
preco_tela_por_metro = 5
perimetro = (c*2)+(l*2)
total_tela = preco_tela_por_metro*perimetro

print(f'O terreno tem {c} metro(s) de comprimento e {l} metro(s) de largura. O perímeto desse terreno tem {perimetro} metro(s). O metro da tela está custando {locale.currency(preco_tela_por_metro, grouping=True)}. Será necessário {locale.currency(total_tela, grouping=True)} para cercar todo o terreno.')
"""
