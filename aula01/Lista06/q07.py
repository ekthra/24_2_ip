email = str(input('Digite seu email:'))
senha = str(input('Digite sua senha:'))
usuario = str(input('Digite seu usuário:'))

if email not in '@.':
    with open('conta.txt', 'a') as conta:
        conta.write(f'{email}\n{senha}\n{usuario}')