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
"""
