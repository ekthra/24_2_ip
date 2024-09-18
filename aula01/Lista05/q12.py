e = int(input('Digite o ataque da espada:'))
e1 = int(input('Digite a durabilidade da espada:'))
l = int(input('Digite o ataque da lança:'))
l1 = int(input('Digite a durabilidade da lança:'))
a = int(input('Digite o ataque do arco:'))
a1 = int(input('Digite a durabilidade do arco:'))

if e > 50 and e1 > 70:
    print('A espada pode ser usada para o combate!')
if l > 50 and l1 > 70:
    print('A lança pode ser usada para o combate!')
if a > 50 and a1 > 70:
    print('O arco pode ser usado para o combate!')
if e <= 50 and e1 <= 70 and a <= 50 and a1 <= 70 and l <= 50 and l1 <= 70 or e <= 50 and e1 >= 70 and a <= 50 and a1 >= 70 and l <= 50 and l1 >= 70:
    print('Sugiro que arrume outras armas!')
elif e >= 50 and e1 <= 70 and a >= 50 and a1 <= 70 and l >= 50 and l1 <= 70:
    print('Sugiro que arrume outras armas!')