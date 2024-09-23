with open('vingadores.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    conteudo = arquivo.read()
for linha in linhas:
    print('{} estou te convidando para uma festa na minha casa!\n'.format(linha))

