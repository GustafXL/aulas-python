from random import randint
from time import sleep
numero = int(input('Em que numero eu estou pensando ? Tente adivinhar um numero entre 0 a 3 '))
n = randint(0, 3)
print('Deixe me pensar...')
sleep(3)
if n == numero:
    print('Voce ganhou ganhou!')
else:
    print('Ocomputador ganhou.')
print(f'O computador pensou em {n}')

