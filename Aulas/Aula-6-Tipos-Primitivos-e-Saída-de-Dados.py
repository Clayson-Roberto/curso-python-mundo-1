# Nessa aula, vamos aprender como funcionam os tipos primitivos no
# Python e as peculiaridades do int() float() bool() e str().
# Além disso, veremos como fazer as primeiras operações com a função print() do Python.

primeiroNumero = int(input('Digite o primeiro número: '))
segundonumero = int(input('Digite o segundo número: '))

# type -> É utilizado para saber o tipo
print(type(primeiroNumero))

somaPrimeiroESegundoNumero = primeiroNumero + segundonumero
print('A soma dos números {} e {} é igual a {}'.format(primeiroNumero,segundonumero,somaPrimeiroESegundoNumero))