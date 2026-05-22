''' O mesmo professor do desafio 19 quer sortear a
ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada. '''

from random import shuffle

aluno01 = input("Digite o nome do primeiro aluno: ")
aluno02 = input("Digite o nome do segundo aluno: ")
aluno03 = input("Digite o nome do terceiro aluno: ")
aluno04 = input("Digite o nome do quarto aluno: ")

listaDeAlunos = [aluno01, aluno02, aluno03, aluno04]
shuffle(listaDeAlunos)

print(f"A sequencia sorteada foi {listaDeAlunos}")



