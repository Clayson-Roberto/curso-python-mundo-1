''' Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. '''

name = input('Digite o nome de uma pessoa: ').strip().lower()

print(f'Este nome tem Silva -> {'silva' in name}')