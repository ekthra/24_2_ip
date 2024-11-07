lista_numeros = []
multiplicador = 0
lista_multiplicada = []
multiplicacao = 0


for i in range(11):
    
    numero = int(input('Digite um número: '))
    
    if i != 10:
        lista_numeros.append(numero)
    
    else:
        multiplicador = numero

for pos in range(len(lista_numeros)):

    numero = lista_numeros[pos]
    multiplicacao = numero * multiplicador

    lista_multiplicada.append(multiplicacao)

print(f'Esta é lista de multiplicações: {lista_multiplicada}')


