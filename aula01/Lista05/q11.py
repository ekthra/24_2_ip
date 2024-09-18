d = float(input('Digite a primeira nota do candidato A:'))
d1 = float(input('Digite a segunda nota do candidato A:'))
d2 = float(input('Digite a primeira nota do candidato B:'))
d3 = float(input('Digite a segunda nota do candidato B:'))
d4 = float(input('Digite a primeira nota do candidato C:'))
d5 = float(input('Digite a segunda nota do candidato C:'))
ma = (d + d1) / 2
mb = (d2 + d3) / 2
mc = (d4 + d5) / 2
if ma > mb and ma > mc:
    print('O candidato A é o vencedor com uma média de: {} pontos!')
elif mb > ma and mb > mc:
    print('O candidato B é o vencedor com uma média de: {}'.format(mb))
elif mc > ma and mc > mb:
    print('O candidato C é o vencedor com uma média de: {}'.format(mc))
elif mc == ma and mc > mb:
    print('Temos um empate entre o candidato A e C, ambos com uma média de {}'.format(ma))
elif mc == mb and ma < mb:
    print('Temos um empate entre o candidato B e C, ambos com uma média de {}'.format(mb))
elif mb == ma and ma > mc:
    print('Temos um empate entre o candidato A e B, ambos com uma média de {}'.format(ma))
else:
    print('Temos um empate triplo!!! os três candidatos com uma média de {}'.format(ma))