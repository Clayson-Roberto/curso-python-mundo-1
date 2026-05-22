# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

num1 = float(input('Primeira nota: '))
num2 = float(input('Segunda nota: '))

calculoMediaNota = (num1 + num2) / 2

print(f"A media das notas deste aluno é {calculoMediaNota:.1f}")