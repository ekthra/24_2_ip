from random import randint

lista_numeros = []

for i in range(0,20):
    aleatorio = randint(1,100)

    if aleatorio not in lista_numeros:

        lista_numeros.append(aleatorio)


numero = int(input('Digite um número: ' ))

print(f'Esta é a lista:\n{lista_numeros}')

for c in range(len(lista_numeros)):

    if numero == lista_numeros[c]:

        lista_numeros.remove(numero)

print(f'Esta é a nova lista sem o {numero}\n{lista_numeros}')
