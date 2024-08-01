# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
from random import choice

words = ['Teste', 'Banana', 'Maçã', 'Laranja', 'Acerola']

forc = choice(words)

print(f'A palavra é: {forc}')