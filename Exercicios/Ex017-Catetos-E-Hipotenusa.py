''' Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa. '''

from math import hypot

caOposto = float(input('Digite o valor do cateto oposto: '))
caAdja = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(caOposto, caAdja)

#Calculando sem usar o modulo math
# -> hipotenusa = (caAdja ** 2 + caOposto ** 2) ** (1/2)

print(f"A Hipotenusa vai medir {hipotenusa:.2f}")
