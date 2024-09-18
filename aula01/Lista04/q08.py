n = int(input('Digite o valor do produto:'))
d1 = n - n * 0.1
d2 = n - n * 0.05
if n > 100:
    print('O produto recebe um desconto de 10%, assim sendo: {}R$'.format(d1))
elif n >= 50 and n <= 100:
    print('O produto recebe um desconto de 5%, assim sendo: {}R$'.format(d2))
else:
    print('O produto não recebe desconto, assim sendo: {}R$'.format(n))
    