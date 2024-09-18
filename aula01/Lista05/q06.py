vr = 0
vr2 = 0
p = 'Primeiro'
s = 'Segundo'
for c in range(1, 3):
    s = float(input('Digite a distância percorrida pelo dragão em KMs:'))
    t = float(input('Digite em quantas horas o dragão percorreu essa distância.'))
    v = s / t
    if c == 1:
        vr = v
        vr2 = v
    else:
        if v > vr:
            vr = v
            print('O segundo dragão é o mais rápido!!!')
        if v < vr2:
            vr2 = v
        if vr > v:
            print('O primeiro dragão é o mais rápido!')
print('tendo uma velocidade de {}km/h, enquanto o outro teve uma velocidade de {}km/h '.format(vr, vr2))