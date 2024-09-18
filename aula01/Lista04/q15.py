km = float(input('Digite a velocidade do carro em km/h:'))
m = (km - 80) * 5
if km < 80:
    print('Você está abaixo do limite!')
elif km == 80:
    print('Você está no limite!')
else:
    print('Você está acima do limite e está multado em {}R$'.format(m))
