# Escreva um programa que converta uma temperatura digitando
# em graus Celsius e converta para graus Fahrenheit.

grauC = float(input("Qual é a temperatura em grau C°: "))

grauF = ((9 * grauC) / 5) + 32

print(f"A temperatura de {grauC}C° corresponde a {grauF}F°")