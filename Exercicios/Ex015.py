# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugado = int(input("Quantos dias alugados? "))
kmRodado = float(input("Quantos Km rodado? "))

valorDia = diasAlugado * 60
valorKm = kmRodado * 0.15

valorTotal = valorDia + valorKm

print(f"Um carro alugado por {diasAlugado} dias alugados e rodado {kmRodado} km ")
print(f"O valor saira por {valorTotal:.2}")