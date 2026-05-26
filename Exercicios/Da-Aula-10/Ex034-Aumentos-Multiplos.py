''' Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores
a R$1250,00, calcule um aumento de 10%. Para os inferiores ou
iguais, o aumento é de 15%. '''

salarioAtual = float(input('Digite o salário do funcionário R$'))
novoSalario = 0

if salarioAtual > 1250:
    novoSalario = ( salarioAtual * 10 / 100 ) + salarioAtual
else:
    novoSalario = ( salarioAtual * 15 / 100 ) + salarioAtual

print(f'O funcionário que recebia R${salarioAtual:.2f} passa a receber R${novoSalario:.2f}')