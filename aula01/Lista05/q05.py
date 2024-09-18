do = float(input('Qual a distância até o oasis?'))
a = float(input('Quantos litros de água você tem?'))

an = do * 2

if a >= an:
    print('Você tem a quantidade de água necessária para chegar até o oasis')
else:
    print('Infelizmente você não tem a quantidade necessária de águe para chegar no oasis')

