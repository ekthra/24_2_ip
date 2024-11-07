from random import randint

lista_numeros = []
maior = 0
posicao_maior = 0
posicao_menor = 0
menor = 0

for c in range(20):
    
    aleatorio = randint(1,100)

    lista_numeros.append(aleatorio)

for numeros in range(len(lista_numeros)):

    aleatorio = lista_numeros[numeros]
    if numeros == 0:

        maior = aleatorio
        menor = aleatorio
        posicao_maior += 1
        posicao_menor += 1
    else:

        if aleatorio > maior:

            maior = aleatorio
            posicao_maior = numeros + 1
        
        if aleatorio < menor:

            menor = aleatorio
            posicao_menor = numeros

print(lista_numeros)

print(f'O maior número da lista é: {maior}\nO menor número da lista é: {menor}\nEstando nas respectivas posições: {posicao_maior}° e {posicao_menor}°')