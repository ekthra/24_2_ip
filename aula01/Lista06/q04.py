from time import sleep
with open("amigos.txt", 'r') as arquivo:
    amigo = arquivo.readlines()
    conteudo = arquivo.read()
for linha in amigo:
    sleep(2)
    print('{}'.format(linha))
