# 14. Encontrar o Maior Número em uma Lista
# Peça ao usuário para digitar uma lista de números e exiba o maior número dessa lista.

numeros = input('Digite número para serem somados: ')

lista_num = list(map(int, numeros.split()))

maior = max(lista_num)

print(f'O maior número nesta lista é: {maior}')