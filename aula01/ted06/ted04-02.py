num_m = int(input('Digite o número de maças compradas:'))
if num_m >= 12:
    valor = num_m
    print('As maças custaram: {}R$'.format(valor))
else:
    valor = num_m * 1.3
    print('As maças custaram: {}R$'.format(valor))