s = float(input('Digite seu salário mensal:'))
im1 = s * 0.15
im2 = s * 0.1
if s <= 2000:
    print('Você está isento do imposto de renda.')
elif s > 3500:
    print('Seu imposto de renda é de: {}R$'.format(im1))
else:
    print('Seu imposto de renda é de: {}R$'.format(im2))
    