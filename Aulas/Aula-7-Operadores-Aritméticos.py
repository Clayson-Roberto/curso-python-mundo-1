# Nessa aula, vamos aprender quais são os operadores aritméticos do
# Python e também sua ordem de precedência dentro de expressões
# matemáticas. Veja como funcionam os operadores de adição,
# subtração, multiplicação, divisão, exponenciação e quociente na
# linguagem Python.


# Adição -> +
# Subtração -> -
# Multiplicação -> *
# Divisão -> /
# Exponenciação ou Potência -> **
# Divisão Inteira -> //
# Modulo oou Resto da Divisão -> %

# Orden de precedência -> Aquilo que deve ser calculado primeiro

# 1 -> ()
# 2 -> **
# 3 -> *, /, //, %
# 4 -> +, -


num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

adicao = num1 + num2
print(f"A soma de {num1} + {num2} é igual a -> {adicao}")

subtracao = num1 - num2
print(f"A subtração de {num1} - {num2} é igual a -> {subtracao} ")

multiplicacao = num1 * num2
print(f"A multiplicação de {num1} * {num2} é igual a -> {multiplicacao}")

divisao = num1 / num2
print(f"A divisão de {num1} / {num2} é igual a -> {divisao}")

potencia = num1 ** num2
print(f"A potencia de {num1} ** {num2} é igual a -> {potencia}")

divisaoInteira = num1 // num2
print(f"A divisão inteira de {num1} // {num2} é igual a -> {divisaoInteira}")

restoDaDivisao = num1 % num2
print(f"O resto da divisão de {num1} % {num2} é igual a -> {restoDaDivisao}")