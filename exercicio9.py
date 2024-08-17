# 9. Verificar Número Primo
# Peça ao usuário para digitar um número e verifique se ele é primo.

num = int(input('Digite um número para verificar se ele é primo: '))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, 'não é primo')
            break
    else:
        print(num, 'é primo')
