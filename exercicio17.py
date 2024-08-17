# 17. Calculando a Sequência de Fibonacci
# Escreva um programa que gera os primeiros 10 números da sequência de Fibonacci.

def fibonacci(num):
    sequencia = [0, 1]
    while len(sequencia) < num:
        prox_num = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_num)
    return sequencia

num = 10
resultado = fibonacci(num)
print(resultado)