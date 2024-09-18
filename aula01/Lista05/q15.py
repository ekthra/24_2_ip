e = int(input('Digite a porcentagem de energia da maquina:'))
a = int(input('Digite quantos anos você quer voltar no tempo:'))
d = int(input('Digite quantos dias você quer voltar no tempo:'))
p = int(input('Escolha uma das capitais que se deseja voltar no tempo.\n[1] Nova York\n[2] Brasilia\n[3] Tokyo\n[4] Paris\n[5] Roma'))
if e > 80 and a == int and a > 0 and d == int and d > 0 and p == 1 or p == 2 or p ==3 or p == 4 or p == 5:
    print('A máquina está pronta para viajar no tempo!')
else:
    print('Desculpe, a maquina não pode ser usada nessas especificações.')
    