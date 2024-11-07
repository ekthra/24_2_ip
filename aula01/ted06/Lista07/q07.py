num = int(input('Digite um número para calcular seu fatorial: '))
multi = num
fator = num - 1
for fatorial in range(0, num -1):
    multi = multi * fator
    fator -= 1
print('O fatorial de {} é igual a {}'.format(num, multi))