# 4. Calculadora Simples
# Crie um programa que peça dois números e a operação desejada(+, -, *, /) e exiba o resultado.

print('Calculadora...Digite os valores e a operação desejada: ')

num1 = int(input('Valor 1: '))
num2 = int(input('Valor 2: '))
operacao = input('Operação: ')

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2 

print(f'O resultado é {resultado}')
