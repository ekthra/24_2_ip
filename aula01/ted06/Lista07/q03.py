frase = str(input('Digite uma frase ou palavra:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
vogal = 0
consoante = 0
for letras in range(len(junto) -1, -1, -1):
    if junto[letras] not in 'AEIOU':
        consoante += 1
    else:
        vogal += 1

print('O número de consoantes é {}, enquanto o de vogais é: {}'.format(consoante, vogal))
    