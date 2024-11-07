num = int(input('Digite um número:'))
resultado = 0
for multiplicador in range(1,11):
    resultado = num * multiplicador
    print(f'{num} x {multiplicador} = {resultado}')
    with open('tabuada2.txt', 'a') as arquivo:
        arquivo.write(f'{num} x {multiplicador} = {resultado}\n')

