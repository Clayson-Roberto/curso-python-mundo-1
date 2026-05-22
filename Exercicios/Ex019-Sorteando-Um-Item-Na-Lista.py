'''Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do quarto aluno: ")
aluno4 = input("Digite o nome do quinto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]
alunoSorteado = random.choice(lista)

print(f"O aluno sorteado foi {alunoSorteado}")