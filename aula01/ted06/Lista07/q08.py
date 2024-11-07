num = int(input('Digite o número em decimal:'))
resto = 0
binario = ""

while num >= 2:
    resto = num % 2
    binario = str(resto) + binario
    num //= 2

binario = str(num) + binario
print(f'{binario} é o número convertido para binário.')