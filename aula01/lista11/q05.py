from random import randint
listaA = []
listaB = []
listasomada = []
soma = 0

for i in range(5):
    aleatorioA = randint(1,100)
    aleatorioB = randint(1,100)

    listaA.append(aleatorioA)
    listaB.append(aleatorioB)

for numero in range(len(listaA)):

    soma = listaA[numero] + listaB[numero]
    listasomada.append(soma)

print(f'Esta é a soma das duas listas:\n{listasomada}')

