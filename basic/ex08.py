# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hora_trabalhada = float(input('Quanto você ganha por hora? '))
hora_mes = float(input('Quantas horas você fez esse mês: '))

salario = hora_trabalhada * hora_mes

print(f'Seu salário vai ser de {salario}')