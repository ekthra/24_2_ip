from random import randint

num = 0
aleatorio = randint(1,100)

while num != aleatorio:
    num = int(input('Irei escolher um número de 1 a 100, tente advinhar!'))
    if num > aleatorio:
        print('Errado, meu número é menor!')
    else:
        print('Errado, meu número é maior!')
print('Parabéns, você venceu, meu número era o {}'.format(aleatorio))