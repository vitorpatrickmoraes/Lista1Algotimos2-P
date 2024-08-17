# 19. Verificar Palíndromo
# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo(lê-se da mesma forma de trás para frente).

def palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()

    if palavra == palavra[::-1]:
        print('A palavra digitada é um palíndromo!')
    else:
        print('A palavra digitada não é um palíndromo!')

palavra = input('Digite uma palavra: ')

print(palindromo(palavra))