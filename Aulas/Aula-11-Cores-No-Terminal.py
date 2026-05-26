''' Nessa aula, vamos aprender como utilizar os códigos
de escape sequence ANSI para configurar cores
para os seus programas em Python. Veja como utilizar
o código \033[m com todas as suas principais possibilidades. '''

# Código para style
'''
0 -> none
1 -> bold
4 -> underline
7 -> negative
'''

# Código para cores da letra
'''
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarela
34 -> azul
35 -> roxo
36 -> azul piscina
37 -> cinza
'''

# Código para cores background
'''
40 -> branco
41 -> vermelho
42 -> verde
43 -> amarela
44 -> azul
45 -> roxo
46 -> azul piscina
47 -> cinza
'''

print('\33[31;42mOlá Mundo!!!\33[m')