# 20. Jogo de Adivinhação
# Crie um programa onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve tentar adivinhar o número. O programa deve dar dicas se o número escolhido é maior ou menor que a tentativa do usuário.
from random import randint

numero_secreto = randint(1, 100)
numero_usuario = int(input('Tente adivinhar o número que estou pensando: '))

while numero_secreto != numero_usuario:
    print('tente novamente!')
    numero_usuario = int(input('Tente adivinhar o número que estou pensando: '))
    if numero_usuario == numero_secreto:
        print('Parabéns, você acertou!')
        break

