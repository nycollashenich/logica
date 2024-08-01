# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

fh = float(input('Informe a temperatura: '))
c = 5 * ((fh - 32)/9)

print(f'Em f° {fh}, em C° {c:.2f}')
