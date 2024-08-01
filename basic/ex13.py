# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

nome = input(str('Digite seu nome: '))
for n in range(len(nome),0,-1):
    print(nome[:n])
