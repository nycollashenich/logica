# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True: 
    try:
        nota = float(input('Digite uma nota entre 0 e 10: '))
        if 0 <= nota <= 10:
            print('Valor correto')
            break
        else:
            print('Valor incorreto')
    except ValueError:
        print('Entrada inválida! Por favor insira um número')