# 15. Números Pares em uma Lista
# Dada uma lista de números, crie um programa que exiba apenas os números pares.

lista_num = [12, 45, 34, 23, 89, 23]
lista_pares = []

for i in lista_num:
    if i % 2 == 0:
        lista_pares.append(i)

print(lista_pares)