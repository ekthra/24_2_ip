f = float(input('Digite a quantidade de ferro em kgs:'))
o = float(input('Digite a quantidade de ouro em kgs:'))
a = o + f
if a / f >= 0.7:
    print('A armadura se saíra perfeitamente!')
else:
    print('Esta armadura irá quebrar!')
    