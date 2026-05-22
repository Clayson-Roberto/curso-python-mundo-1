# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input("Digite um valor em metros: "))

centimetro = metro * 100
milimetro = metro * 1000

print(f"O valor de {metro} em centimetro é igual a -> {centimetro}")
print(f"O valor de {metro} em milimetros é igual a -> {milimetro}")