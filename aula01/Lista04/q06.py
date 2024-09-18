nc = int(input('Digite o número da sua conta:'))
d = float(input('Digite o débito:'))
s = float(input('Digite seu saldo:'))
c = float(input('Digite seu crédito:'))
sa = s - d + c
if sa > 0:
    print('[ SALDO POSITIVO ]  O Saldo Atual da conta {} é de {}R$'.format(nc, sa))
elif sa < 0:
    print('[ SALDO NEGATIVO ]  O Saldo Atual da conta {} é de {}R$'.format(nc, sa))
else:
    print('[ SALDO NEUTRO ]  O Saldo Atual da conta {} é de {}R$'.format(nc, sa))