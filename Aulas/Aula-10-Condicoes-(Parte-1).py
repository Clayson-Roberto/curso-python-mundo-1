''' Nessa aula, vamos aprender como utilizar estruturas
condcionais simples e compostas nos seus programas em Python. '''


print(f'{'-' * 25}Iniciando com condicionais{'-' *25}')
nomeTeste01 = input('Digite seu nome: ')

# Quando não tem "else" na condição chamamos condição simples, se existir condição composta
if nomeTeste01 == 'Clayson':
    print('Que nome lindo você tem')
else:
    print('Que nome comum você tem')
print(f'Prazer em te conhecer {nomeTeste01}')

print(f'{'-' * 25}Finalizando com condicionais{'-' *25}')


print(f'{'-' * 25}Iniciando com teste de notas{'-' *25}')

nota1Teste01 = float(input('Digite sua primeira nota: '))
nota2Teste01 = float(input('Digite sua segunda nota: '))
mediaTeste01 = (nota1Teste01 + nota2Teste01) / 2

if mediaTeste01 >= 6.0:
    print(f'Uma média na nota de {mediaTeste01} é uma boa nota')
else:
    print(f'Uma média de nota {mediaTeste01} não é boa estude mais')

print(f'{'-' * 25}Iniciando com teste de notas{'-' *25}')