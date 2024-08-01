# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Informe o raio do circulo: '))
area = math.pi * raio ** 2
print(f'A área do círculo é {area} e o seu diamêtro é igual a {2 * raio}')