num = 0
cont = 0
soma = 0

while num != 999:
    
    num = int(input('Digite a nota do aluno:\n (Digite 999 para finalizar o programa) '))
    cont += 1
    soma += num

media = (soma - 999) / (cont - 1)

print('A média do aluno foi de: {} pontos'.format(media))
