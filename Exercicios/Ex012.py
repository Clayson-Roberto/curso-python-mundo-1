# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Digite o valor do produto: "))

desconto = valor - (valor * 5 / 100)

print(f"O produto com o valor de {valor} com o desconto de 5% é igual a -> {desconto}")