''' Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento
de String, Análise com len(), count(), find(),
transformações com replace(), upper(), lower(), capitalize(),
title(), strip(), junção com join(). '''


''' FATIAMENTO '''
frase = "Curso em Vídeo Python"

print(f"{15 * '-'} Fatiamento {15 * '-'}")
# Fatia a frase pegando apenas o caractere que
# esta na posição que esta dentro de colchetes
print(f"A frase fatiada na posição 6 é -> {frase[6]}")

# Fatia a frase pegando apenas os caracteres da posição 3 e indo até a posição 10
print(f"A frase fatiada da posição 3 até a posição 10 é -> {frase[3:10]}")

# Fatia a frase pegando apenas os caracteres da posição 3 e indo até
# a posição 10 pulando de 2 em 2
print(f"A frase fatiada da posição 3 até a posição 10 pulando de 2 em 2 é -> {frase[3:10:2]}")

# Divide a frase em um lista e numerando cada palavra como um item da lista
print(f"Utilizado para separar cada palavra em um item de uma lista -> {frase.split()}")


''' ANÁLIZE '''
print(f"{15 * '-'} Análise {15 * '-'}")

# .count() -> Serve para contar quantas vezes aperece o caractere
# referenciado dentro de parenteses
print(f"Contagem de quantas vezes aparece a letra 'o' em frase -> {frase.count('o')}")

# Usado 'len()' para saber o tamanho da frase
print(f"Tamanho total da frase usando 'len()' -> {len(frase)}")

# O '.find()' é usado para localizar em qual posição se encontra a palavra ou letra desejada
print(f"Mostra em que posição esta a palavra que esta sendo pedida no caso 'deo' -> {frase.find('deo')}")

# O "'palavra' in frase" serve para saber se existe a palavra em alguma parte da string
print(f"Utilizado para saber se existe a palavra em alguma parte da string -> {'Curso' in frase}")

''' TRANSFORMAÇÕES '''
print(f"{15 * '-'} Transformações {15 * '-'}")

# O '.strip()' remove os espações que estão no início da frase e do final
print(f"Usado '.strip()' para remover espaços indesejados na frase -> {frase.strip()}")

# Usado para deixar a frase toda com as letras em caixa alta
print(f"A frase fica toda em caixa alta com o método .upper() -> {frase.upper()}")

# Usado para deixar a frase toda com as letras em caixa baixa
print(f"A frase fica toda em caixa baixa com método .lower() -> {frase.lower()}")

# Usado para deixar apenas a primeira letra da frase em caixa alta o restante
# fica em caixa baixa
print(f"A frase fica toda em caixa baixa apenas a primeira letra em caixa alta -> {frase.capitalize()}")

# Usado '.replace(old, new)' troca a palavra old pela new
print(f"Usando .replace() para altera Python por Android -> {frase.replace('Python', 'Android')}")

# Usado '.title()' para deixar todas as palavras da frase com a primeira letra em caixa alta
print(f"Usando .title() para que todas a palavras da frase iniciem com a letra em caixa alta -> {frase.title()}")

''' JUNÇÃO '''
print(f"{15 * '-'} Junção {15 * '-'}")

fraseLista = frase.split()

# O " '-'.join(fraseLista) " é utilizado para juntar os itens de uma lista
# em um string o caractere que estiver em aspas sera o separador
print(f"Utilizado para juntar os itens de uma lista tranformando em uma string -> {' '.join(fraseLista)}")