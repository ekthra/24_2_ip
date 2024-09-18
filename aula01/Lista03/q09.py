s = 1
p = 1
for c in range(1, 3):
    n = int(input('Digite um número:'))
    if c == 1:
        p = n
    if c == 2:
        s = n       
    r = p / s
print('A divisão do primeiro número pelo segundo é {}'.format(r))

