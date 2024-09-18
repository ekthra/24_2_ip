g1a = int(input('Digite o ataque do primeiro guerreiro:'))
g1d = int(input('Digite a defesa do primeiro guerreiro:'))
g2a = int(input('Digite o ataque do segundo guerreiro:'))
g2d = int(input('Digite a defesa do segundo guerreiro:'))
g1all = g1a + g1d
g2all = g2a + g2d

if g1all > g2all:
    print('O primeiro guerreiro é o vencedor!!!')
elif g2all > g1all:
    print('O segundo guerreiro é o vencedor!!!')
elif g2all == g1all and g1d > g2d:
    print('O primeiro guerreiro é o vencedor!!!')
elif g2all == g1all and g1d < g2d: 
    print('O segundo guerreiro é o vencedor!!!')
else:
    print('A batalha ocasionou em empate!!!')