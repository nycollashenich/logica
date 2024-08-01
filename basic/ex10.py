string1 = 'Brasil Hexa 2006'
string2 = 'Brasil! Hexa 2006!'
print(f'Tamanho da string: {string1} é de: {len(string1.strip())} caracteres') 
print(f'Tamanho da string: {string2} é de: {len(string2.strip())} caracteres')

if len(string1) == len(string2):
    print('As duas tem o mesmo número de caracteres')
else:
    print('Os tamanhos são diferentes.')