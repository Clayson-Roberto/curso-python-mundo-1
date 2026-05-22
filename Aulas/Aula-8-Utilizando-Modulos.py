# Nessa aula, vamos aprender como utilizar módulos em
# Python utilizando os comandos import e from/import no Python.
# Veja como carregar bibliotecas de funções e utilizar
# vários recursos adicionais nos seus programas utilizando
# módulos built-in e módulos externos, oferecidos no Pypi.

# Importa todas os modulos interno de " math " para utiliza-ló
# basta colocar math. ele mostrará quais modulos ele possui, se caso
# esejar importar apenas um modulo basta utilizar o modo " from "
# from math import sqrt, ceil
import math

num = int(input("Digite um numero: "))

raiz = math.sqrt(num)

print(f"A raiz quadrada de {num} é {math.ceil(raiz)}")


# Importa modulo para sortear numeros
import random

numRandom = random.randint(1, 10)

print(f"Número sorteado pelo modulo random -> {numRandom}")


# Importa modulo para utilizar emotions
import emoji

print(emoji.emojize("Ola mundo 😋"))