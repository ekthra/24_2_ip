qa = int(input('Digite a quantidade atual do produto em estoque:'))
qm = int(input('Digite a quantidade máxima do produto em estoque:'))
qmi = int(input('Digite a quantidade minima do produto em estoque:'))
qme = (qm + qm) / 2
if qa < qme:
    print('Efetuar a compra.')
else:
    print('Não efetuar a compra.')
