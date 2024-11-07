num = 1000
print('Estes são todos o números de 1000 a 2000, que quando dividido por 11 o resto é igual a 5')

for multi in range(0, 1001):
    if num % 11 == 5:
        print(num, end=' ')
    num += 1