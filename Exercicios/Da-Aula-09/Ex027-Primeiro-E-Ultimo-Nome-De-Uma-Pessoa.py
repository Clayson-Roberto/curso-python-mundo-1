''' Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente. '''

nome = input('Digite o nome de uma pessoa: ').strip()

print(f'Seu primeiro nome é -> {nome.split()[0].capitalize()}')
print(f'Seu último nome é -> {nome.split()[-1].capitalize()}')