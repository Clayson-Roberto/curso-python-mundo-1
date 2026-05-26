''' Escreva um programa que leia a velocidade de um carro. Se ele
ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. '''

velocidadeDoCarro = int(input('Qual a velocidade do carro: '))
if velocidadeDoCarro > 80:
    valorPorKm = (velocidadeDoCarro - 80) * 7
    print(f'''Você excedeu o limite de velocidade de 80km por hora!
A uma velocidade de {velocidadeDoCarro}km por hora a multa será de R${valorPorKm:.2f}''')
print('Tenha um bom dia!!! Dirija com segurança!!!')

