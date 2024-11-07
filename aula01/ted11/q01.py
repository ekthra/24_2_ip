lista_numeros = []

for i in range(10):
    numero = int(input('Digite um número: '))
    lista_numeros.append(numero)

organizado = sorted(lista_numeros)
contador = 0.132
contador2 = 0
repetidos = False
posicao = []

for num in range(len(organizado)):
    numero = organizado[num]
    if numero == contador:
        repetidos = True
        for c in range(len(lista_numeros)):
            if lista_numeros[c] == numero:
                contador2 = c + 1
                posicao.append(contador2)

    contador = organizado[num]

if repetidos:
    print(f'Existem números repetidos! Aqui está a lista de posições dos números repetidos:\n{posicao} ')

else:
    print('Não existem números repetidos!')        





