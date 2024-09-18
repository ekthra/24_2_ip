n = int(input('Digite um número'))
n2 = int(input('Digite outro número'))

if n2 > n:
    print('O maior número foi o {}'.format(n2))
elif n > n2:
    print('O maior número foi o {}'.format(n))
else:
    print('Os dois números são iguais')
    