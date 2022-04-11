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

real = 2
cotacao_dolar = 4.70
print(f'{real} reais está custando hoje {cotacao_dolar*real} dólares.')

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

valor = 80
desconto_porcentagem = 12
total = valor*((100-desconto_porcentagem)/100)
print(f'O procuto custa {valor} reais e com desconto de {desconto_porcentagem}% passa a custar {total}.')

# 38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.

salario = 1200
aumento_porcentagem = 25
novo_salario = salario*((aumento_porcentagem/100)+1)
print(f'O funcionário recebe {salario} reais, com aumento de {aumento_porcentagem}% seu salário foi para {novo_salario} reais.')


# 39 - A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# -> O primeiro gahador receberá 46%;
# -> O segundo receberá 32%;
# -> O terceiro receberá o restante;

premiacao_total = 780000
primeiro_lugar = 46
segundo_lugar = 32
terceiro_lugar = 100-primeiro_lugar-segundo_lugar
valor_primeiro = premiacao_total*(primeiro_lugar/100)
valor_segundo = premiacao_total*(segundo_lugar/100)
valor_terceiro = premiacao_total*(terceiro_lugar/100)

print(f'O primeiro ganhador levou {valor_primeiro} reais, o segundo ganhador levou {valor_segundo} reais e o terceiro levou {valor_terceiro} reais!')
"""
