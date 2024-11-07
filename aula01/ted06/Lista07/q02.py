num = int(input('Digite um número para sua tabuada:'))
for tabuada in range(1,11):
    print('{} x {} = {}'.format(num, tabuada, num * tabuada))
print('Esta é a tabuada de {}'.format(num))