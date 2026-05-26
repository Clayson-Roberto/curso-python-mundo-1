''' Escreva um programa que faça o computador “pensar” em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. '''

from random import randint
from time import sleep

print(f'{'-=' * 50}')
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print(f'{'-=' * 50}')

numComputer = randint(0, 5)
numUser = int(input('Em qual número eu pensei: '))

print('Pensando...')
sleep(2)

if numComputer == numUser:
    print(f'Fenomenal você acertou eu pensei justamente no {numComputer}')
else:
    print(f'Que pena eu pensei no número {numComputer}, mais sorte na proxima')

print('Fim do Programa !!!')
