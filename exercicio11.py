# 11. Tabuada
# Peça ao usuário para digitar um número e imprima a tabuada desse número de 1 a 10.

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 10 + 1):
    tab = num * i 
    print(f'{num} x {i} = {tab}')