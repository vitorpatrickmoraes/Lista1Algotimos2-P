# 8. Contagem de Números Ímpares
# Escreva um programa que conta e imprime todos os números ímpares entre 1 e 100.

count = 0
for i in range(1, 100):
    if i % 3 == 0:
        print(i)
        count += 1
        

print(f'A quantidade de números ímpares foi: {count}')