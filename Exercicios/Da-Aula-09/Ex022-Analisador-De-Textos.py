''' Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome. '''

name = input("Digite seu nome: ").strip()

print("Analizando seu nome...")
print(f"Seu nome em maiúculas é -> {name.upper()} ")
print(f"Seu nome em minúsculas é -> {name.lower()} ")
print(f"Seu primeiro nome tem ao todo {len(name.split()[0])} letras")
print(f"Seu nome completo tem ao todo {len(name) - name.count(' ')} letras")
print(f"Seu primeiro nome é {name.split()[0]} ")