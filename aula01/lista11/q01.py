lista_times = []

for c in range(5):
    times = str(input('Digite um time de futebol: '))

    lista_times.append(times)

time_coração = str(input('Qual o seu time do coração?'))

iguais = False

for time in range(len(lista_times)):

    if lista_times[time].upper() == time_coração.upper():

        iguais = True

if iguais:

    print('Achei!!!')
else:

    print('Não achei!!!')
    