''' Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. '''

cidade = input('Digite o nome de uma cidade: ').strip().lower().split()

print(cidade[0] == "santo")
