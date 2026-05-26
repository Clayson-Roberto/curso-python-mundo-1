# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite um valor que tem na carteira R$: "))
dolar = real / 5.00

print(f"Com {real} reais você pode comprar {dolar:.2f} dolares")