# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
result = 0
notas = []

for n in range(0,4):
    nota = float(input('Informe a nota: '))
    result += nota / 4
    notas.append(nota)

print(f'As nota foram {notas}')
print(f'E a media foi {result:.2f}')