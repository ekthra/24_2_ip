m = float(input('Quantas moedas de 1 real você tem?'))
n = float(input('Quantas moedas de 50 centavos você tem?'))
s = float(input('Quantas moedas de 25 centavos você tem?'))
c25 = 0.25 * s
c50 = 0.5 * n
t = m + c25 + c50
print('Você tem no total {}R$'.format(t))
