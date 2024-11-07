num = int(input('Digite um número:'))
cont = 0
for c in range(1, num +1):
    if num % c == 0:
        cont += 1
    if num == 1:
        cont += 1
if cont == 2:
    print('O número {}, é um número primo!'.format(num))
else:
    print('O número {},  não é um número primo!'.format(num))