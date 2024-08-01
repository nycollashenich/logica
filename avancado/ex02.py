# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# def cadastrar():
#     while True:
#         email = input('Informe seu email: ').upper()
#         senha = input('Agora, sua senha: ').upper()

#         if email == senha:
#             print('A senha não pode ser a mesma que o email')
#         else:
#             print('Usuário cadastrado')
#             break

# cadastrar()



def cadastro():
    while True:
            email = input('Informe seu email: ').upper()
            senha = input('Informe sua senha: ').upper()
            
            if senha == email:
                print('A senha não pode ser igual ao email')
            else:
                print('Cadastro feito com sucesso.')
                break
cadastro()