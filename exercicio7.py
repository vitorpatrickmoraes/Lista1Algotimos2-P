# 7. Fatorial de um Número
# Peça ao usuário para digitar um número e calcule o fatorial desse número.

def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    return fat

numero = int(input('Digite um número para obter seu fatorial: '))
resultado = fatorial(numero)
print(f'O fatorial do número digitado foi: {resultado}')
