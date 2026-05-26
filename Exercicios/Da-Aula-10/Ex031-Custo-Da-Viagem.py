''' Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 parta viagens mais longas. '''

kmDaViagem = int(input('Qual a distancia da viagem: '))

print(f'Você está prestes a começar uma vigem de {kmDaViagem}Km!')
preco = kmDaViagem * 0.50 if kmDaViagem <= 200 else kmDaViagem * 0.45
print(f'E o preço da sua viagem será de R$ {preco:.2f}')