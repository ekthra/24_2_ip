m = 0
s = 0
for c in range(1,3):
    a = float(input('Digite a nota do aluno:'))
    m = m + a
    s = m / 2
if m >= 6:
    print('Parabéns, sua média foi {}, você está aprovado.'.format(s))
else:
    print('Infelizmente, você está reprovado com uma média de {}'.format(s))
