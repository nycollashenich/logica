# Faça um Programa que converta metros para centímetros.

transf = input('Cm ou M: ').upper()
num = float(input('Informe o valor: '))

if transf == 'M':
    cm = num * 100
    print(f'O valor {num} em cm é {cm}')
elif transf == 'CM':
    m = num / 100
    print(f'O valor {num} em M é {m}')
else:
    print('Valor incorreto.')