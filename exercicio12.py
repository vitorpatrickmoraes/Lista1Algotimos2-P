# 12. Contar Vogais em uma String
# Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.



def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

print(conta_vogais(str(input('Digite uma string: '))))