m = int(input('Digite o número de missões que o cavaleiro completou:'))
if m > 10:
    print('O cavaleiro deve receber um bonus de 100 moedas de ouro!')
elif m < 5:
    print('O cavaleiro deve receber um bonus de 10 moedas de ouro!')
else:
    print('O cavaleiro deve receber um bonus de 50 moedas de ouro!')
    