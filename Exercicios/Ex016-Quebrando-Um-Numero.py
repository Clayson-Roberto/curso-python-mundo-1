# Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua Porção Inteira.

from math import trunc

num = float(input("Digite um numero real: "))
porcaoInteira = trunc(num)

print(f"A porção inteira de {num} é {porcaoInteira}")