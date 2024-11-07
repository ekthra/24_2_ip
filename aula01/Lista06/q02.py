cont = 1
num = 1
resultado = 0

for tabuada in range(1, 101):
    resultado = num * cont
    print(num, 'x', cont, '=', resultado)
    with open('Tabuada.txt', 'a') as arquivo:
        arquivo.write(f'{num} x {cont} = {resultado}\n')
    cont += 1
    if cont > 10:
        cont = 1
        num += 1
    
    