# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

msn = input("Digite algo: ")

print(f"O tipo primitivo deste valor é {type(msn)}")
print(f"Só tem espaços: {msn.isspace()}")
print(f"É um número: {msn.isnumeric()}")
print(f"É alfabetico: {msn.isalpha()}")
print(f"É alfanumerico: {msn.isalnum()}")
print(f"Esta em maiuscula: {msn.isupper()}")
print(f"Esta em minuscula: {msn.islower()}")
print(f"Esta capitalizada: {msn.istitle()}")