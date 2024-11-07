cont = 0
with open("celebridades.txt", 'r') as arquivo:
    celebridade = arquivo.readlines()
    conteudo = arquivo.read()
for linha in celebridade:
    cont += 1
    if cont % 2 != 0 or cont > 5:
        print('\nVocê foi convidado para o meu aniversário {}\n'.format(linha))
    if cont % 2 == 0 and cont < 5:
         print('{} não poderá vir\n'.format(linha))
