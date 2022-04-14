'''
# 01 - Faça um programa que receba dois números e mostre qual deles é o maior.

n1 = 8
n2 = 7

if n1 > n2:
    print(f'{n1} é maior que {n2}!')
else:
    print(f'{n2} é maior que {n1}!')

# 02 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.

n = int(input('Digite um número inteiro positivo ou negativo: '))

if n >= 0:
    raiz = n ** 0.5
    print(f'O número {n} é positivo e a raiz quadrada dele é {raiz}.')
else:
    print(f'O número {n} não é positivo.')
    
'''
