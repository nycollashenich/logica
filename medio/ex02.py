
'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    while True:    
        nome = input('Seu nome: ')
        if len(nome) > 3:
            break   
        else:
            print('Nome inválido')

    while True:
        try:
            idade = int(input('Sua idade: '))
            if 0 <= idade <= 150:
               break
            else: 
                print('A idade deve estar entre 0 e 150')
        except ValueError:
            print('Insira um número')
    
    while True:
        try:
            salario = float(input('Seu salário: R$ '))
            if salario > 0:
                break
            else:
                print('O salário deve ser maior que 0')
        except ValueError:
            print('Salário inválido.')
    
    while True: 
        try:
            sexo = input('F ou M: ').upper()
            if sexo in ['F', 'M']:
                break
            else:
                print('Digite um valor válido')
        except ValueError:
            print('Valor inválido.')    
    
    while True:
        try: 
            estado_civil = input('S, C, V, D: ').upper()
            if estado_civil in ['S', 'C', 'V', 'D']:
                break
            else:
                print('Digite um valor válido.')
        except:
            print('Valor inválido')

    break

print(f'Seu nome é {nome}')
print(f'Sua idade é {idade}')
print(f'Seu salário é R${salario}')
print(f'Seu sexo é {'femino' if sexo == 'F' else 'masculino'}')
print(f'Seu estado civil é {estado_civil}')

    