from random import randint

dado = str(input('Deseja rolar um dado de 6 lados? [S/N]')).strip().upper()

if dado not in 'SN':
    print('Escolha inválida')
elif dado == 'S':
    while dado not in 'N':
        valor = randint(1,6)
        print('Você tirou {} no dado!'.format(valor))
        dado = str(input('Deseja rolar o dado de 6 lados novamente? [S/N]')).strip().upper()
        if dado not in 'SN':
            print('Escolha inválida')
            dado = 'N'
print('Finalizando o programa.')
