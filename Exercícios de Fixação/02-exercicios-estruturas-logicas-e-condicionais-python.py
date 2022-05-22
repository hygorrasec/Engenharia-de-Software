'''
# 01 - Faça um programa que receba dois números e mostre qual deles é o maior.

n1 = 8
n2 = 10

if n1 > n2:
    print(f'{n1} é maior que {n2}!')
elif n1 < n2:
    print(f'{n2} é maior que {n1}!')
else:
    print(f'{n1} e {n2} são iguais!')

# 02 - Leia um número fornecido pelo usuário. Se o número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

n = int(input('Digite um número real positivo ou negativo: '))

if n >= 0:
    raiz = n ** 0.5
    print(f'O número {n} é positivo e a raiz quadrada dele é {raiz}.')
else:
    print(f'O número {n} é inválido.')

# 03 - Leia um número real. Se o número for positivo, imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.

n = -9
if n >= 0:
    raiz = n**0.5
    print(f'O número {n} é positivo e a raiz quadrada dele é {raiz}.')
else:
    ao_quadrado = n**2
    print(f'O número {n} ao quadrado será {ao_quadrado}.')

# 04 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# 1: O número digitado ao quadrado;
# 2: A raiz quadrada do número digitado.

n = 9
if n >= 0:
    ao_quadrado = n**2
    raiz = n**0.5
    print(f'O número {n} ao quadrado será {ao_quadrado}. E sua raiz é {raiz}.')
else:
    print(f'O número {n} não é positivo.')

# 05 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

n = 9
mod = n % 2

if mod == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')

# 06 - Escreva um programa que, dados dos números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

n1 = 10
n2 = 10

if n1 > n2:
    diferenca = n1 - n2
    print(f'{n1} é maior que {n2} e a diferença entre eles é {diferenca}!')
elif n1 < n2:
    diferenca = n2 - n1
    print(f'{n2} é maior que {n1} e a diferença entre eles é {diferenca}!')
else:
    print(f'{n1} e {n2} são iguais!')

# 07 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "números iguais".

n1 = 9
n2 = 7

if n1 > n2:
    print(f'{n1} é o maior!')
elif n1 < n2:
    print(f'{n2} é o maior!')
else:
    print(f'{n1} e {n2} são números iguais!')

# 08 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor de 0.0 a 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.

nota1 = 8
nota2 = 10
media = (nota1+nota2)/2

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    print(f'A nota 1 foi "{nota1}" e a nota 2 foi "{nota2}". A média foi: {media}.')
else:
    print('Um das notas não é válida.')

# 09 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima "Empréstimo não concedido", caso contrário imprima: "Empréstimo concedido".

salario = 1200
emprestimo = 200
porcentagem_salario = salario * 0.2

if emprestimo > porcentagem_salario:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')

# 10 - Faça um programa que receba a altura e o sexo de uma pessoa, calcule e mostre seu peso ideal utilizando as seguintes fórmulas (onde h corresponde à altura):
# - Homem: (72.7 * h) - 58
# - Mulher: (62.1 * h) - 44.7

altura = 1.68
sexo = 'h' # h = homem | m = mulher

if sexo == 'h':
    formula = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {formula}kg.')
elif sexo == 'm':
    formula = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {formula}kg.')

# 11 - Escreva um programa que leia um número inteiro maior do que zero e devolva na tela a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor de 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".

n = 294
lista = []
total = 0

for i in str(n):
    lista.append(i)
    total = total + int(i)

if n > 0:
    print(f'A soma dos números {lista} é igual a {total}.')
else:
    print('Número inválido.')

'''

