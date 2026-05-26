''' Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas
podem ou não formar um triângulo. '''

reta01 = float(input('Digite o valor da primeira reta: '))
reta02 = float(input('Digite o valor da segunda reta: '))
reta03 = float(input('Digite o valor da terceira reta: '))

if reta01 < reta02 + reta03 and reta02 < reta03 + reta01 and reta03 < reta01 + reta02:
    print('As retas passadas podem formar um triângulo')
else:
    print('As retas passadas não podem formar um triângulo')

print(3 * 5 + 4 ** 2)