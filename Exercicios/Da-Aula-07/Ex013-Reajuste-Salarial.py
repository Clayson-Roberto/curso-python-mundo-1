# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salarioAtual = float(input('Qual o salário do funcionario? R$ '))

novoSalario = salarioAtual + (salarioAtual * 15 / 100)

print(f"O salário de um funcionário que ganha R$ {salarioAtual}, com aumento de 15%")
print(f"Será de R$ {novoSalario:.2f}")