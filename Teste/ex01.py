maior = 0
menor = 0
alturatotal = 0
contadorf = 0
media = 0

for pessoa in range(0, 15):
    altura = int(input('Qual sua altura em centimetros?'))
    genero = int(input('Qual seu gênero? [M = 1] [F = 2]'))
    if genero == 2:
        contadorf += 1
    alturatotal += altura
    if pessoa == 0:
        maior = altura
        menor = altura
    else:
        if maior < altura:
            maior = altura
        if menor > altura:
            menor = altura

media = alturatotal/15

print(f'A média de altura é de: {media}cm\nA maior altura é de:{maior}cm\nA menor altura é de: {menor}cm\nO número de mulheres a realizar o programa é de: {contadorf}. ')

    
