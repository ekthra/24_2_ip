t = int(input('Digite um dos lados do triangulo:'))
t2 = int(input('Digite o outro lado do triangulo:'))
t3 = int(input('Digite o ultimo lado do triangulo:'))

if abs(t - t2) < t3 < t2 + t:
    if t == t2 == t3:
        print('Esse é um triangulo EQUILÁTERO')
    elif t != t2 != t3 != t:
        print('Esse é um triangulo ESCALENO')
    else:
        print('Esse é um triangulo ISÓCELES') 
else:
    print('Esses valores não podem formar um triangulo.')
